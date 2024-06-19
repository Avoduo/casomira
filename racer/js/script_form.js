document.querySelector('#form_submit').addEventListener('submit', () => {
    event.preventDefault(); 
    const name_value = document.querySelector('input#fname').value;

    if (name_value === '') {
        alert('Nevypsal si jméno!');
      } 
    else {
        console.log(name_value);
    }

    /*document.write(`Díky za přihlášení ${name_value}!`) */

  });

  document.querySelector('#fname').addEventListener('input', () => {
    event.preventDefault(); 

    let diky = document.querySelector('input#fname').value;

    if (diky === '') {
        thanks.textContent = '';
      } 
    else {
        thanks.textContent = 'Díky za přihlášení, ' + diky + '!';
    }
    
  });