document.addEventListener('DOMContentLoaded', function() {
    const saveButton = document.getElementById('saveLink');
    const savedLinksDiv = document.getElementById('savedLinks');
  
    // 저장된 링크 표시
    function displayLinks() {
      chrome.storage.sync.get(['links'], function(result) {
        const links = result.links || [];
        savedLinksDiv.innerHTML = '<h3>Saved Links:</h3>';
        links.forEach(function(link, index) {
          savedLinksDiv.innerHTML += `
            <a href="${link.url}" target="_blank">${link.title}</a>
          `;
        });
      });
    }
  
    // 초기 링크 목록 표시
    displayLinks();
  
    // 링크 저장 버튼 클릭 이벤트
    saveButton.addEventListener('click', function() {
      chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        const currentTab = tabs[0];
        chrome.storage.sync.get(['links'], function(result) {
          const links = result.links || [];
          links.push({url: currentTab.url, title: currentTab.title});
          chrome.storage.sync.set({links: links}, function() {
            displayLinks();
          });
        });
      });
    });
  });