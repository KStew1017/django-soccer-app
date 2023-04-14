const nav = document.querySelector('.matchday-navbar ul');
const spanElements = document.querySelectorAll('[id^="matchday"]');
const matchdayElements = document.querySelectorAll('.matchday');

// Hide all span elements except the active one on page load
const activeMatchdayId = nav.querySelector('.active').id;
spanElements.forEach(span => {
  const matchdayId = span.id.replace('matchday', '');
  if (matchdayId !== activeMatchdayId && matchdayId !== '') {
    span.classList.add('hide');
  }
});

// Add click event listener to each li element with class 'matchday'
matchdayElements.forEach(li => {
  li.addEventListener('click', () => {
    // Remove the 'active' class from all li elements
    matchdayElements.forEach(li => {
      li.classList.remove('active');
    });

    // Add the 'active' class to the clicked li element
    li.classList.add('active');

    // Hide all span elements except the active one
    const activeMatchdayId = li.id;
    spanElements.forEach(span => {
      const matchdayId = span.id.replace('matchday', '');
      if (matchdayId !== activeMatchdayId && matchdayId !== '') {
        span.classList.add('hide');
      } else {
        span.classList.remove('hide');
      }
    });
  });
});


const searchInput = document.querySelector('[data-search]')
const matchList = document.querySelectorAll('.match-card')
searchInput.addEventListener('input', (e) => {
  const searchValue = e.target.value.toLowerCase()
  matchList.forEach(match => {
    const matchup = match.querySelector('.matchup').textContent.toLowerCase()
    const homeTeamName = match.querySelector('.home-team-logo').alt.toLowerCase()
    const awayTeamName = match.querySelector('.away-team-logo').alt.toLowerCase()
    const isVisible = matchup.includes(searchValue) || homeTeamName.includes(searchValue) || awayTeamName.includes(searchValue)
    match.classList.toggle('hide', !isVisible)
  })
});