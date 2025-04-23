async function runSearch() {
  const res = await fetch('/search_index.json');
  const index = await res.json();

  const input = document.createElement('input');
  input.type = 'text';
  input.placeholder = 'Search...';
  input.style = 'width: 100%; padding: 0.5rem; font-size: 1rem;';
  document.getElementById('searchbox').appendChild(input);

  input.addEventListener('input', () => {
    const query = input.value.toLowerCase().trim();
    const results = index.filter(entry =>
      entry.keywords.some(kw => kw.includes(query))
    );

    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = results.length
      ? results.map(r => `<p><a href="${r.url}">${r.title}</a></p>`).join('')
      : '<p><em>No matches</em></p>';
  });
}

runSearch();
