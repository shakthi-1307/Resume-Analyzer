async function analyzeResume() {
  console.log("Button clicked!");

  const jd = document.getElementById("jd").value;
  const fileInput = document.getElementById("resumeFile");
  const resultsArea = document.getElementById("resultsArea");
  const btn = document.getElementById("analyzeBtn");
  const btnText = document.getElementById("btnText");
  const loader = document.getElementById("loader");

  if (!fileInput.files[0] || !jd) {
    alert("Please provide both a Job Description and a Resume.");
    return;
  }

  // Show loading state
  btn.disabled = true;
  btnText.innerText = "AI is thinking...";
  loader.classList.remove("hidden");

  const formData = new FormData();
  formData.append("job_description", jd);
  formData.append("resume", fileInput.files[0]);

  try {
    // Set a 5-minute timeout for the analysis (LLM can be slow)
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 300000); // 5 minutes

    const response = await fetch("/analyze", {
      method: "POST",
      body: formData,
      signal: controller.signal
    });

    clearTimeout(timeout);

    if (!response.ok) {
      try {
        const errorData = await response.json();
        console.error("Server Error:", errorData);
      } catch (e) {
        console.error("Server Error:", response.status, response.statusText);
      }
      alert("Server Error: " + response.status + ". Check browser console.");
      return;
    }

    const data = await response.json();
    console.log("Response received:", data);

    // Validate response data
    if (!data.match_score || !data.analysis) {
      console.error("Invalid response format:", data);
      alert("Invalid response from server. Check console.");
      return;
    }

    // Update UI
    document.getElementById("matchScore").innerText = data.match_score;
    document.getElementById("aiFeedback").innerHTML = data.analysis.replace(
      /\n/g,
      "<br>",
    );
    resultsArea.classList.remove("hidden");

  } catch (error) {
    console.error("Error during analysis:", error);
    
    if (error.name === "AbortError") {
      alert("Request timed out. The AI took too long to respond. Try again or check if Ollama is running.");
    } else if (error instanceof TypeError) {
      alert("Could not connect to the backend. Is FastAPI running on http://127.0.0.1:8000?");
    } else {
      alert("An error occurred: " + error.message);
    }
  } finally {
    btn.disabled = false;
    btnText.innerText = "Analyze Now";
    loader.classList.add("hidden");
  }
}
