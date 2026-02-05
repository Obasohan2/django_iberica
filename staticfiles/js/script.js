function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener('DOMContentLoaded', function () {
  const likeBtn = document.getElementById('like-btn');
  if (!likeBtn) return;

  likeBtn.addEventListener('click', function () {
    fetch(likeBtn.dataset.url, {
      method: 'POST',
      headers: {
        'X-CSRFToken': getCookie('csrftoken'),
        'X-Requested-With': 'XMLHttpRequest'
      }
    })
    .then(res => res.json())
    .then(data => {
      if (data.error) return;

      document.getElementById('like-count').textContent = data.likes;

      const icon = likeBtn.querySelector('i');
      icon.classList.toggle('fas', data.liked);
      icon.classList.toggle('far', !data.liked);
    })
    .catch(console.error);
  });
});