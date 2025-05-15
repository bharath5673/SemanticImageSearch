# 🔍 Semantic Image Search with CLIP and FAISS

This project demonstrates a **semantic image search engine** powered by [CLIP (Contrastive Language-Image Pretraining)](https://openai.com/research/clip) and [FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss), wrapped in an intuitive [Streamlit](https://streamlit.io) interface.

Users can upload a folder of images and search for relevant results using free-form natural language prompts.

## 🚀 Features

- **Visual-AI search** powered by the [Ultralytics `solutions.VisualAISearch`](https://docs.ultralytics.com/guides/similarity-search/)
- Upload a folder of your own images
- Zero-shot text-based search (no need for training)
- Streamlit-based UI
- Real-time top-k image results with similarity scores

## 🧠 Advantages of Using CLIP + FAISS

<p align="center">
  <img src="https://github.com/ultralytics/docs/releases/download/0/clip-image-retrieval.avif" alt="CLIP Image Retrieval Workflow" width="45%" />
  <img src="https://github.com/ultralytics/docs/releases/download/0/faiss-indexing-workflow.avif" alt="FAISS Indexing Workflow" width="45%" />
</p>

### ✅ Zero-Shot Capabilities
You don't need to train the model on your specific dataset. CLIP's zero-shot learning lets you perform search queries on any image dataset using free-form natural language, saving both time and resources.

### 🧠 Human-Like Understanding
Unlike keyword-based search engines, CLIP understands semantic context. It can retrieve images based on abstract, emotional, or relational queries like `"a happy child in nature"` or `"a futuristic city skyline at night"`.

> _Powered by OpenAI CLIP’s language-image embedding capabilities._

### 🏷️ No Need for Labels or Metadata
Traditional image search systems require carefully labeled data. This approach only needs raw images — CLIP generates embeddings without requiring manual annotation.

### ⚡ Flexible and Scalable Search
FAISS enables fast nearest-neighbor search even with large-scale datasets. It's optimized for speed and memory, allowing real-time response even with thousands or millions of embeddings.

> _Meta FAISS powers scalable embedding-based retrieval pipelines._

### 🌐 Cross-Domain Applications
Whether you're building:
- A personal photo archive
- A creative inspiration tool
- A visual product search engine
- An art or meme recommendation system  
…this stack adapts to diverse domains with minimal tweaking.

## 📦 Requirements

- Python 3.8+
- `ultralytics` 
- `streamlit`

Install all dependencies:
```bash
pip install ultralytics streamlit
```

run:
```bash
streamlit run test_SIS.py
```


<video width="640" height="360" controls>
  <source src="simplescreenrecorder-2025-05-15_19.31.01.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


