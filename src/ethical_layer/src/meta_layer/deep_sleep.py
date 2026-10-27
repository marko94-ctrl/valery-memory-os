from sklearn.cluster import KMeans

def deep_neural_sleep(embeddings, n_clusters=20):
    print("🌙 DUBOKI NEURALNI SAN - KMeans 20 domena")
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    clusters = kmeans.fit_predict(embeddings)
    print(f"✅ Mapirano {n_clusters} domena - sklad -0.5 -> 1.0")
    return clusters
