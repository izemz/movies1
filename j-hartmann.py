from transformers import pipeline

# Duygu analizi pipeline'ını yükle
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Duyguları sınıflandırmak için fonksiyon
def analyze_emotions(text):
    result = emotion_classifier(text)
    return result

# Filtrelenmiş dosyayı aç ve her satır için duygu analizi yap
def analyze_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            if line.startswith('D:') or line.startswith('N:'):
                emotion = analyze_emotions(line)
                # Sonuçları dosyaya yaz
                outfile.write(f"{line.strip()} => {emotion[0]['label']} (Confidence: {emotion[0]['score']:.2f})\n")

    print("Duygu analizi tamamlandı. Sonuçlar yeni dosyada kaydedildi.")

input_file = r'C:\Users\zaimi\Desktop\MOVIES\scripts\parsed\tagged\ZOOTOPIA_filtered.txt'  
output_file = r'C:\Users\zaimi\Desktop\MOVIES\scripts\parsed\tagged\ZOOTOPIA_emotion_analysis_result.txt'  

analyze_file(input_file, output_file)
