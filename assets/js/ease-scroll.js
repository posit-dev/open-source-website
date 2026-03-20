/**
 * Smoothly scrolls to a position (or bottom) with easing and a startup delay.
 * @param {number|null} targetY - Pixel to scroll to (null for bottom).
 * @param {number} duration - Animation time in ms.
 * @param {number} delay - Time to wait before starting in ms.
 */
async function easeScroll({ targetY = null, duration = 800, delay = 0 } = {}) {
  // 1. Handle the delay
  if (delay > 0) {
    console.log(`Waiting ${delay}ms before scrolling...`);
    await new Promise(resolve => setTimeout(resolve, delay));
  }

  const startY = window.scrollY;
  const pageHeight = document.documentElement.scrollHeight - window.innerHeight;
  const finalTarget = targetY !== null ? targetY : pageHeight;
  const difference = finalTarget - startY;
  let startTime = null;

  // Ease-In-Out-Cubic formula
  const easing = (t) => t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;

  function animation(currentTime) {
    if (startTime === null) startTime = currentTime;
    const timeElapsed = currentTime - startTime;
    const progress = Math.min(timeElapsed / duration, 1);

    window.scrollTo(0, startY + (difference * easing(progress)));

    if (timeElapsed < duration) {
      requestAnimationFrame(animation);
    } else {
      console.log("Scroll complete.");
    }
  }

  console.log("Scrolling started!");
  requestAnimationFrame(animation);
}
