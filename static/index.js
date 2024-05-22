

async function getAll() {
try {
  const response = await fetch("/get", {
    method:'GET'
  });
  const data = await response.json();
  const items = data.items

  const list = document.getElementById('list')
// Create list
  for (var i = 0; i < items.length; i++) {
      const el = items[i]
      const li = document.createElement('li');
      const delbut = document.createElement("BUTTON");
      li.innerHTML = el.name;
      li.appendChild(delbut);
      console.log(li);
      list.append(li);
      delbut.addEventListener("click", delUno);

  }
 


} catch (error) {
 console.log(error) 
}
}
// -------------------------
async function delUno() {
  console.log("jeeeee")
  try {
    const response = await fetch("/delete", {
      method:'DELETE'
    });
    const data = await response.json();
    const items = data.items

    for (var i = 0; i < items.length; i++) {
        const el = items[i]
        const li = document.createElement('li');
        li.innerHTML = el.name;
        console.log(li);
        list.append(li);
    }

  } catch (error) {
    console.log(error) 
  }
}

getAll()





