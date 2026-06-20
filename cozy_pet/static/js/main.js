// cozy pet - main.js
// 後の Issue でステータス更新・インタラクション処理を実装する

document.addEventListener('DOMContentLoaded', () => {
  console.log('cozy pet loaded');

  // data-width 属性からゲージ幅を設定（CSP 'unsafe-inline' 排除のため）
  document.querySelectorAll('.status-bar[data-width]').forEach(el => {
    el.style.width = el.dataset.width + '%';
  });
});
