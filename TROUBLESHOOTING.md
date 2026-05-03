# Troubleshooting Guide

## Error: "Uncaught (in promise) Error: A listener indicated an asynchronous response..."

This error occurs when the backend request times out or doesn't respond properly. Here's how to fix it:

### Solution 1: Ensure Ollama is Running and Responsive

1. **Start Ollama service:**

   ```bash
   ollama serve
   ```

   You should see output like:

   ```
   2024/05/02 10:30:00 loaded the model successfully
   ```

2. **Test Ollama directly:**

   ```bash
   ollama list
   ```

   Should show:

   ```
   NAME        ID              SIZE    MODIFIED
   mistral     sha256:abc...   4.1 GB  2 hours ago
   ```

3. **Test the endpoint:**
   ```bash
   curl http://127.0.0.1:11434/api/tags
   ```

### Solution 2: Check Browser Console (F12)

1. Open **Developer Tools** (F12)
2. Go to **Console** tab
3. Look for detailed error messages
4. Check the **Network** tab to see failed requests

### Solution 3: Verify FastAPI Server is Running

1. Check that the FastAPI server started without errors
2. Open browser and go to: `http://127.0.0.1:8000`
3. You should see the Resume Analyzer UI
4. If not, check the terminal where FastAPI is running for errors

### Solution 4: Increase Timeout for Large Resumes

The current timeout is 5 minutes. If your resume is very large:

1. Edit `static/js/script.js`
2. Find this line: `const timeout = setTimeout(() => controller.abort(), 300000);`
3. Change `300000` to a larger value (in milliseconds):
   - `600000` = 10 minutes
   - `900000` = 15 minutes

### Solution 5: Check System Resources

1. **CPU/Memory:** Ollama needs adequate resources. Open Task Manager and check:
   - CPU usage (should not be maxed out)
   - Memory usage (Ollama + Python need ~4GB+)

2. **Disk Space:** Ensure you have at least 5GB free space

### Solution 6: Restart Everything

1. Close FastAPI terminal (Ctrl+C)
2. Stop Ollama (Ctrl+C)
3. Close browser
4. Restart Ollama: `ollama serve`
5. In new terminal, restart FastAPI: `python -m app.main`
6. Refresh browser (Ctrl+Shift+R for hard refresh)

## Common Issues

| Issue                     | Cause                             | Solution                                          |
| ------------------------- | --------------------------------- | ------------------------------------------------- |
| "Timeout" error           | Ollama is slow or not responding  | Restart Ollama, check if model needs to be pulled |
| "Could not connect" error | FastAPI not running               | Run `python -m app.main`                          |
| "Invalid response" error  | Server returned unexpected format | Check FastAPI logs                                |
| Blank UI                  | Static files not found            | Ensure `static/` folder is in root directory      |

## Performance Tips

1. **First run is slow** - The AI model loads on first use (15-30 seconds)
2. **Large PDFs take longer** - More text = more analysis time
3. **GPU vs CPU** - If available, use GPU for faster processing
4. **Model selection** - Mistral is faster than larger models like Llama2

## Debugging Steps

1. Open browser console (F12)
2. Click "Analyze Now"
3. Watch the console for:
   - "Button clicked!" message
   - Network request to `/analyze`
   - Response from server
   - Error messages

## Still Having Issues?

1. Check the README.md installation steps
2. Ensure Python 3.8+ is installed
3. Verify all dependencies: `pip list | grep -E "fastapi|pdfplumber|ollama"`
4. Try with a different/smaller PDF file
5. Check if Ollama model is corrupted: `ollama rm mistral && ollama pull mistral`

## Contact/Support

For more help:

- Check Ollama documentation: https://ollama.ai
- FastAPI docs: https://fastapi.tiangolo.com
- Check browser console (F12) for detailed error messages
