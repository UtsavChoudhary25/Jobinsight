/**
 * JobInsight API Service Client
 * Connects frontend views to the FastAPI Machine Learning & NLP Backend.
 * Supports:
 * 1. Dedicated Backend URL via VITE_API_URL (e.g. Hugging Face Spaces / Render)
 * 2. Same-origin Vercel Serverless Functions (/api/...)
 * 3. Local development fallback (http://localhost:8000)
 */

const getBaseUrl = () => {
  if (import.meta.env.VITE_API_URL) {
    return import.meta.env.VITE_API_URL.replace(/\/+$/, '');
  }
  // If in browser production on Vercel, use relative URL (same-origin)
  if (typeof window !== 'undefined' && window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1') {
    return '';
  }
  // Local development fallback
  return 'http://localhost:8000';
};

const BASE_URL = getBaseUrl();

export async function checkBackendHealth() {
  try {
    const res = await fetch(`${BASE_URL}/health`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    });
    if (!res.ok) throw new Error(`Health check failed (${res.status})`);
    return await res.json();
  } catch (err) {
    return { status: 'offline', error: err.message, model_loaded: false, nlp_ready: false };
  }
}

export async function getModelMetadata() {
  try {
    const res = await fetch(`${BASE_URL}/api/model-info`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    });
    if (!res.ok) throw new Error(`Failed to fetch model metadata (${res.status})`);
    return await res.json();
  } catch (err) {
    console.error("Error fetching model info:", err);
    throw err;
  }
}

export async function predictSalary(payload) {
  try {
    const res = await fetch(`${BASE_URL}/api/predict-salary`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      throw new Error(errData.detail || `Prediction failed with status ${res.status}`);
    }
    return await res.json();
  } catch (err) {
    console.error("Salary prediction error:", err);
    throw err;
  }
}

export async function extractSkills(description) {
  try {
    const res = await fetch(`${BASE_URL}/api/extract-skills`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ description }),
    });
    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      throw new Error(errData.detail || `NLP extraction failed with status ${res.status}`);
    }
    return await res.json();
  } catch (err) {
    console.error("NLP extraction error:", err);
    throw err;
  }
}
