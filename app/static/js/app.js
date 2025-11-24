// Custom JavaScript for InsightPilot
// HTMX handles most interactivity

// Add any global utilities here
console.log('InsightPilot loaded');

// Copy to clipboard utility (for invite links later)
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(
    () => {
      console.log('Copied to clipboard');
      // Could show a toast notification here
    },
    (err) => {
      console.error('Failed to copy:', err);
    }
  );
}

// Make it available globally
window.copyToClipboard = copyToClipboard;
