import matplotlib.pyplot as plt
from collections import defaultdict

# Giriş dosyasının adı
input_file = r'C:\Users\zaimi\Desktop\MOVIES\script2\7emotions\ZOOTOPIA_emotions.txt'

# Duygu analizi sonuçlarını saklamak için bir defaultdict
emotion_scores = defaultdict(list)

# Dosyayı oku ve her satırdaki duygu ve güven skorunu işle
with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        # Duygu ve güven skorunu çıkartmak için satırdaki yazıyı ayıkla
        if "=>" in line:
            text, emotion_data = line.split(" => ")
            emotion, score_data = emotion_data.split(" (Confidence: ")
            score = float(score_data.replace(")", "").strip())

            # Duygu ve güven skorunu listeye ekle
            emotion_scores[emotion.strip()].append(score)

# Ortalama güven skorlarını hesapla
average_scores = {emotion: sum(scores) / len(scores) for emotion, scores in emotion_scores.items()}

# Toplam duygu sayısını hesapla
total_emotions = sum(len(scores) for scores in emotion_scores.values())

# Yüzde dağılımını hesapla
emotion_percentages = {emotion: (len(scores) / total_emotions) * 100 for emotion, scores in emotion_scores.items()}

# Sonuçları yazdır
print("Ortalama Güven Skorları:")
for emotion, avg_score in average_scores.items():
    print(f"{emotion.capitalize()}: {avg_score:.2f}")

print("\nYüzde Dağılımı:")
for emotion, percentage in emotion_percentages.items():
    print(f"{emotion.capitalize()}: {percentage:.2f}%")

# Pasta grafiği için duygu ve yüzde verilerini ayır
labels = list(emotion_percentages.keys())
sizes = list(emotion_percentages.values())

plt.figure(figsize=(8, 8))
colors = ['#1C7D81', '#AAAAAA', '#C7CD74', '#446EB6', '#FDEB4C', '#D893B7', '#F2A953']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'fontsize': 10})
plt.axis('equal')
plt.show()

# Sabit bir duygu sırası belirle
emotion_order = ["joy", "sadness", "fear", "anger", "disgust", "surprise", "neutral"]

# Bu sıraya göre bir vektör oluştur
script_vector = [emotion_percentages.get(emotion, 0) / 100 for emotion in emotion_order]

print("\nScript vector (normalized):", script_vector)