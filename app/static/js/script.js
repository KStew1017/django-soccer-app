// const matchdays = document.querySelectorAll('.matchday');

// matchdays.forEach(matchday => {
//     matchday.addEventListener('click', () => {
//         document.querySelector('.active').classList.remove('active');
//         matchday.classList.add('active');

//         const nav = document.querySelector('.matchday-navbar ul');
//         const activeMatchdayId = nav.querySelector('.active').id;
//         document.querySelectorAll('[id^="matchday"]').forEach(span => {
//             const matchdayId = span.id.replace('matchday', '');
//             if (matchdayId !== activeMatchdayId && matchdayId !== '') {
//                 span.classList.toggle('hide');
//             }
//         });
//     });
// });


// const nav = document.querySelector('.matchday-navbar ul');
// const activeMatchdayId = nav.querySelector('.active').id;
// document.querySelectorAll('[id^="matchday"]').forEach(span => {
//     const matchdayId = span.id.replace('matchday', '');
//     if (matchdayId !== activeMatchdayId && matchdayId !== '') {
//         span.classList.toggle('hide');
//     }
// });


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
