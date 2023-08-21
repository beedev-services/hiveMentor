const stageBar = document.getElementById('stageBar')

const canUseStorage = storageAvailable('localStorage')

let projectDataAvailable

if (canUseStorage) {
    if (localStorage.getItem('projectStore')) {
        let projectStore = JSON.parse(localStorage.getItem('projectStore'));
    if(projectStore.title !== '') {
        printProjectTitle(projectStore.title);
    }
    projectDataAvailable = true;
    buildRetrievedProject();
    } else {
        projectDataAvailable = false;
    }
}
else {
    alert('localStorage is not available. As a result, project data will cannot be saved. For project reloading between sessions, please allow localStorage in your browser settings or update your browser version.');
}
updateProgress()

document.addEventListener('keyup', function(event){
    if (event.target.matches('#new-col-title')) {
        const input = document.getElementById('new-col-title');
        const createColBtn = document.getElementById('create-col-btn');
        if(input.value.length > 0) {
            createColBtn.removeAttribute('disabled');
        } else {
            createColBtn.setAttribute('disabled', 'true');
        }
    }
})

document.addEventListener('click', function(event){
    const btnID = event.target.id;
    const elementNumber = getColNumber(btnID);
    let appendEl;
    if (event.target.matches('#save-project-name')) {
        saveProjectTitle();
    }
    if (event.target.matches('#edit-project-name')) {
        editProjectTitle();
    }
    if (event.target.matches('.add-card-btn')) {
        openAddCardForm(elementNumber);
    }
    if (event.target.matches('#add-col-div')) {
        const modal = document.getElementById('modal');
        if (!modal.classList.contains('open')){
            openAddColumn(elementNumber);
        }
    }
  if (event.target.matches('#create-col-btn')) {
    const newColTitle = document.getElementById('new-col-title').value;
    const newColTracking = document.getElementById('new-col-tracking').getAttribute('data-tracking');
    addColumn(newColTitle, newColTracking);
  }
  if (event.target.matches('.open-col-menu-btn') || event.target.matches('.open-card-menu-btn')) {
		appendEl = document.getElementById('submenuBody');
		if (!appendEl.hasChildNodes()) {
	      openEditSubMenu(event.target, elementNumber);
	    }
	}
	if (event.target.matches('#choose-tracking')) {
	  openTrackingOptions();
	}
	if (event.target.matches('.optionDiv')) {
	  const chosenValue = event.target.children[0].value;
	  const chosenText = event.target.children[0].getAttribute('data-text');
	  assignNewColTracking(chosenValue, chosenText);
	}
	if (event.target.matches('#update-col-' + elementNumber)) {
	  updateColumnTitle(elementNumber);
	}
	if (event.target.matches('.delete-col-btn')) {
	  deleteColumn(elementNumber);
	}
	if (event.target.matches('.update-card-btn')) {
	  updateCardText(elementNumber);
	}
	if (event.target.matches('.col-tool')){
	  if (event.target.id == 'open-edit-col-' + elementNumber) {
	      openColEdit(elementNumber);
	  }
	  if (event.target.id == 'delete-col-' + elementNumber) {
	    openDeleteWarning(elementNumber);
	  }
	}
	if (event.target.matches('.card-tool')){
	  if (event.target.id == 'open-edit-card-' + elementNumber) {
	      openCardEdit(elementNumber);
	  }
	  if (event.target.id == 'delete-card-' + elementNumber) {
	    deleteCard(elementNumber);
	  }
	}
	if (event.target.matches('#close-modal') || event.target.matches('#cancel-modal-action')) {
	  closeModal();
	}
	if (event.target.matches('#close-col-menu')) {
	  closeSubMenu();
	}
	if (event.target.matches('#add-card-' + elementNumber)) {
	  addCard(elementNumber);
	}
	if (event.target.matches('#remove-add-card-form-' + elementNumber)) {
	  closeAddCardForm(elementNumber);
	}
});
document.addEventListener('dragstart', function(event){
    beingDragged(event);
});
document.addEventListener('dragover', function(event){
  let dragging = document.querySelector('.dragging');
  if (dragging.classList.contains('card')) {
    cardDrag(event);
  }
  if (dragging.classList.contains('col')) {
    colDrag(event);
  }
});
document.addEventListener('dragend', function(event){
  dragEnd(event);
});
document.addEventListener('drop', function(event){
  dragDrop(event);
  //updateProgress();
});

function beingDragged(ev) {
  ev.dataTransfer.setData("text/plain", ev.target.id);
  const draggedEl = ev.target;
  draggedEl.classList.add("dragging");
}
function cardDrag(ev) {
  ev.preventDefault();
  ev.dataTransfer.dropEffect = "move";
  let data = ev.dataTransfer.getData("text/plain");
  let draggedEl;
  if (data !== '') { // For Firefox
    draggedEl = document.getElementById(data);
  } else { // For Chrome
    draggedEl = document.querySelector('.dragging');
  }
  const dragOver = ev.target;
  const dragOverParent = dragOver.parentElement;
  const beingDragged = document.querySelector(".dragging");
  const draggedParent = beingDragged.parentElement;
  const project = document.getElementById("project");
  const draggedIndex = whichChild(beingDragged);
  const dragOverIndex = whichChild(dragOver);
  if (dragOver.classList.contains('card')) {
    if (draggedParent === dragOverParent) {
      if (draggedIndex < dragOverIndex) {
        draggedParent.insertBefore(dragOver, draggedEl);
      }
      if (draggedIndex > dragOverIndex) {
        draggedParent.insertBefore(dragOver, draggedEl.nextSibling);
      }
    }
    if (draggedParent !== dragOverParent) {
      dragOverParent.insertBefore(draggedEl, dragOver);
    }
  }
  if (dragOver.classList.contains('cardsContainer')) {
    colDraggedOver(ev);
  }
}
function colDrag(ev) {
  ev.preventDefault();
  ev.dataTransfer.dropEffect = "move";
  const dragOver = ev.target;
  const columnContainer = document.getElementById('columnsContainer');
  let data = ev.dataTransfer.getData("text/plain");
  let draggedEl;
  if (data !== '') { // For Firefox
    draggedEl = document.getElementById(data);
  } else { // For Chrome
    draggedEl = document.querySelector('.dragging');
  }
  const draggedIndex = whichChild(draggedEl);
  const dragOverIndex = whichChild(dragOver);

  if (draggedEl.id !== dragOver.id && dragOver.classList.contains('col')) {
    if (draggedIndex < dragOverIndex) {
      columnContainer.insertBefore(dragOver, draggedEl);
    }
    if (draggedIndex > dragOverIndex) {
      columnContainer.insertBefore(dragOver, draggedEl.nextSibling);
    }
  }

}
function dragEnd(ev) {
  const draggedEl = ev.target;
  const newTracking = draggedEl.parentNode.getAttribute('data-track')
  draggedEl.classList.remove("dragging");
  draggedEl.setAttribute('data-card-track', newTracking);
  updateProgress();
}
function dragDrop(ev) {
  ev.preventDefault();
}
function colDraggedOver(ev) {
  ev.dataTransfer.dropEffect = "move"
  const dragOver = ev.target;
  const updatedTrackng = dragOver.getAttribute('data-track');
  //const beingDragged = document.querySelector(".dragging");
  let data = ev.dataTransfer.getData("text/plain");
  let draggedEl;
  if (data !== '') {   // For Firefox

    draggedEl = document.getElementById(data);
  } else {   // For Chrome
    draggedEl = document.querySelector('.dragging');
  }
  const draggedParent = draggedEl.parentElement;
  if (draggedParent.id !== dragOver.id && draggedParent.classList.contains('cardsContainer') && dragOver.classList.contains('cardsContainer')) {
    let dragOverChildCount = dragOver.childElementCount;
    let dragOverLastChild = dragOver.children[dragOver.childElementCount - 1];
    if (dragOverChildCount === 0 || ev.clientY > dragOverLastChild.offsetTop + dragOverLastChild.offsetHeight ) {
      dragOver.appendChild(draggedEl);
      dragOver.setAttribute('data-card-track', updatedTrackng);
    }
  }
}
function whichChild(el) {
  let i = 0;
  while ((el = el.previousSibling) !== null) ++i;
  return i;
}
function updateProgress() {
  const stageBar = document.getElementById('stageBar');
  const allCards = document.getElementsByClassName('card');
  const doneCards = document.querySelectorAll('.card[data-card-track="done"]');
  const inProgressCards = document.querySelectorAll('.card[data-card-track="in-progress"]');
  const cardContainers = document.getElementsByClassName('cardsContainer');
  const totals = document.getElementsByClassName('total');
  const doneBar = document.createElement('div');
  const inProgressBar = document.createElement('div');
  while (stageBar.hasChildNodes()) {
    stageBar.removeChild(stageBar.firstChild);
  }
  for (let h = 0; h < cardContainers.length; h++) {
    let cardCount = cardContainers[h].querySelectorAll('.card').length;
    totals[h].innerText = cardCount;
  }
  doneBar.classList.add('done-gradient');
  inProgressBar.classList.add('in-progress-gradient')
  doneBar.style.width = ((200/allCards.length) * doneCards.length) + 'px';
  inProgressBar.style.width = ((200/allCards.length) * inProgressCards.length) + 'px';
  stageBar.appendChild(doneBar);
  stageBar.appendChild(inProgressBar);
  updateProjectData();
}
function storageAvailable(type) {
    try {
        var storage = window[type],
            x = '__storage_test__';
        storage.setItem(x, x);
        storage.removeItem(x);
        return true;
    }
    catch(e) {
        return e instanceof DOMException && (
            // everything except Firefox
            e.code === 22 ||
            // Firefox
            e.code === 1014 ||
            // test name field too, because code might not be present
            // everything except Firefox
            e.name === 'QuotaExceededError' ||
            // Firefox
            e.name === 'NS_ERROR_DOM_QUOTA_REACHED') &&
            // acknowledge QuotaExceededError only if there's something already stored
            storage.length !== 0;
    }
}
function updateProjectData() {
  const allCols = document.getElementsByClassName('col');
  let projectStore;
  if (projectDataAvailable) {
    projectStore = JSON.parse(localStorage.getItem('projectStore'));
  }
  let update;
  let projectData = [];
  for (let i = 0; i < allCols.length; i++) {
    let cardData = [];
    let cards = allCols[i].querySelectorAll('.card');
    let colNumber = getColNumber(allCols[i].id);
    let colTitle = allCols[i].querySelector('.col-name').innerText;
    let colTracking = allCols[i].getAttribute('data-track');

    for (let k = 0; k < cards.length; k++) {
      let cardNumber = getColNumber(cards[k].id);
      let cardText = cards[k].querySelector('#card-text-' + cardNumber).innerText;
      let card = new Card(cardNumber, cardText);
      cardData.push(card);
    }
    let col = new Column(colNumber, colTitle, colTracking, cardData);
    projectData.push(col);
  }
  if (projectDataAvailable) {
    update = new Project(projectStore.title, projectData, projectStore.runningColCount)
  } else {
    update = new Project('', projectData, allCols.length)
  }
  localStorage.setItem('projectStore', JSON.stringify(update));
}
function buildRetrievedProject() {
  const projectData = JSON.parse(localStorage.getItem('projectStore'));
  const colContainer = document.getElementById('columnsContainer');
  const columns = document.getElementsByClassName('col');
  while(columns.length > 0) {
    columns[0].parentNode.removeChild(columns[0]);
  }
  const projectHTML = `${projectData.data.map((col, i) =>
      `<div id="stage-${col.colNumber}" class="col ${col.tracking}-gradient ${col.tracking}-border" data-track="${col.tracking}" draggable="true">
        <div class="colHeader">
          <div id="total-${col.colNumber}" class="total ${col.tracking}-border"></div><h2 class="col-name">${col.colTitle}</h2>
          <button id="addCard-${col.colNumber}" class="add-card-btn col-btn" title="Add a card to this column">
            <img src="https://res.cloudinary.com/anthony-dee/image/upload/v1546548847/noun_Plus_869750_no_attribute.svg" alt="Add a card to this column" />
          </button>
          <button id="open-col-menu-${col.colNumber}" class="open-col-menu-btn col-btn" title="Open column edit menu">
            <img src="https://res.cloudinary.com/anthony-dee/image/upload/v1546548847/noun_ellipsis_869758_no_attribute.svg" alt="Open column edit menu" />
          </button>
        </div>
        <div id="cards-${col.colNumber}" class="cardsContainer" data-track="${col.tracking}">
          ${col.cards.map((card, i) =>
            `<div id="card-${card.cardNumber}" class="card" draggable="true" data-card-track="${col.tracking}">
                <div id="card-text-${card.cardNumber}" class="card-text">${card.cardText}</div>
              <button id="open-card-menu-${card.cardNumber}" class="open-card-menu-btn card-btn" title="Open card edit menu">
                <img src="https://res.cloudinary.com/anthony-dee/image/upload/v1546548847/noun_ellipsis_869758_no_attribute.svg" alt="Open card edit menu" />
              </button>
            </div>`
          ).join('')}
        </div>
      </div>`
    ).join('')}`;
  colContainer.insertAdjacentHTML('afterbegin', projectHTML);
}
function Project(title, data, runningColCount) {
  this.title = title;
  this.data = data;
  this.runningColCount = runningColCount;
}
function Column(colNumber, colTitle, colTracking, cards) {
  this.colNumber = colNumber;
  this.colTitle = colTitle;
  this.tracking = colTracking;
  this.cards = cards;
}
function Card(cardNumber, cardText) {
  this.cardNumber = cardNumber;
  this.cardText = cardText;
}
function getColNumber(str) {
  let slicedStr = str.slice(str.lastIndexOf('-') + 1);
  return slicedStr;
}
function saveProjectTitle() {
  let projectStore = JSON.parse(localStorage.getItem('projectStore'));
  let projectTitle = document.getElementById('project-title-text').value;
  let update;
  if (projectTitle === '') {
    alert('Please enter a project title');
  } else {
    update = new Project(projectTitle, projectStore.data);
    localStorage.setItem('projectStore', JSON.stringify(update));
    printProjectTitle(projectTitle);
  }
}
function editProjectTitle() {
  const titleInput = document.getElementById('project-title-text');
  const saveTitleBtn = document.getElementById('save-project-name');
  const titleH2 = document.getElementById('project-title');
  const editTitleBtn = document.getElementById('edit-project-name');
  titleH2.setAttribute('hidden', true);
  editTitleBtn.setAttribute('hidden', true);
  titleInput.removeAttribute('hidden');
  saveTitleBtn.removeAttribute('hidden');
  titleInput.value = localStorage.getItem('projectTitle');
  titleInput.focus();
}
function printProjectTitle(title) {
  const titleInput = document.getElementById('project-title-text');
  const saveTitleBtn = document.getElementById('save-project-name');
  const titleH2 = document.getElementById('project-title');
  const editTitleBtn = document.getElementById('edit-project-name');
  titleInput.setAttribute('hidden', true);
  saveTitleBtn.setAttribute('hidden', true);
  titleH2.innerText = title;
  titleH2.removeAttribute('hidden');
  editTitleBtn.removeAttribute('hidden');
}
function openEditSubMenu(btn, elementNumber) {
  let submenuPosX, submenuPosY;
  const submenu = document.getElementById('sub-menu');
  const submenuBody = document.getElementById('submenuBody');
  const editOptionsHTML = `
    <ul>
      <li>
        <a id="open-edit-${btn.classList.contains('col-btn') ? 'col' : 'card'}-${elementNumber}" class="${btn.classList.contains('col-btn') ? 'col' : 'card'}-tool">Edit ${btn.classList.contains('col-btn') ? 'column' : 'card'}</a>
      </li>
    </ul>
    <ul>
      <li>
        <a id="delete-${btn.classList.contains('col-btn') ? 'col' : 'card'}-${elementNumber}" class="${btn.classList.contains('col-btn') ? 'col' : 'card'}-tool">Delete ${btn.classList.contains('col-btn') ? 'column' : 'card'}</a>
      </li>
    </ul>
  `;
  submenuBody.innerHTML = editOptionsHTML;
  submenu.removeAttribute('hidden');
  submenuPosX = btn.offsetLeft - (submenu.offsetWidth * 0.9) + 15;
  submenuPosY = btn.offsetTop + 30;
  submenu.style.left = submenuPosX + 'px';
  submenu.style.top = submenuPosY + 'px';
  submenu.style.display = 'block';
}

function openTrackingOptions(){
  let submenuPosX, submenuPosY;
  const buttonPressed = document.getElementById('choose-tracking');
  const modal = document.getElementById('modal');
  const submenu = document.getElementById('sub-menu');
  const menuHead = document.getElementById('submenuHeader');
  const menuTitle = document.getElementById('submenuTitle');
  const menuBody = document.getElementById('submenuBody');
  let newColTracking = document.getElementById('new-col-tracking').getAttribute('data-tracking');
  const trackingOptions = [
    { optionTitle: 'None', optionText: 'This column will not be automated',dataTracking: 'none' },
    { optionTitle: 'To do',optionText: 'Planned but not started',dataTracking: 'to-do'},
    { optionTitle: 'In progress', optionText: 'Actively being worked on', dataTracking: 'in-progress'},
    { optionTitle: 'Done', optionText: 'Items are complete', dataTracking: 'done'}
  ];
  menuTitle.innerText = 'Select type';
  if (menuBody.childElementCount === 0) {
    const optionsHTML = `${trackingOptions.map((item,i) =>
      `<div class="optionDiv">
        <input id="track-option-${i + 1}" type="radio" name="new-tracking-type" class="tracking-type" value="${item.dataTracking}" hidden="tru" data-text="${item.optionTitle}" />
        <div class="checkDiv">
          <span class="trackingCheck">${item.dataTracking == newColTracking ? `&#10003;` : ''}</span>
          <label for="track-option-${i + 1}">${item.optionTitle}</label>
        </div>
        <span class="trackingDesc">${item.optionText}</span>
      </div>`
    ).join('')}`;
    menuBody.innerHTML = optionsHTML;
  }
  menuHead.removeAttribute('hidden');
  submenu.removeAttribute('hidden');
  submenu.style.width = 'auto';
  submenuPosX = ((window.innerWidth/2) - (modal.offsetWidth / 2) + 16);
  submenuPosY = (window.innerHeight/4) + buttonPressed.offsetTop + buttonPressed.offsetHeight;
  submenu.style.left = submenuPosX + 'px';
  submenu.style.top = submenuPosY + 'px';
  submenu.style.display = 'block';
}
function assignNewColTracking(value, text) {
  const newColTracking = document.getElementById('new-col-tracking');
  newColTracking.setAttribute('data-tracking', value);
  newColTracking.innerText = text;
  closeSubMenu();
}
function updateColumnTitle(column) {
  const colTitle = document.querySelector('#stage-' + column + ' .col-name');
  const newColTitle = document.getElementById('update-col-text-' + column).value;
  colTitle.innerText = newColTitle;
  updateProjectData();
  closeModal();
}
function deleteColumn(column) {
  const columnsContainer = document.getElementById('columnsContainer');
  const stageColumn = document.getElementById('stage-' + column);
  columnsContainer.removeChild(stageColumn);
  closeModal();
  updateProgress();
}
function closeSubMenu() {
  const submenu = document.getElementById('sub-menu');
  const submenuBody = document.getElementById('submenuBody');
  const menuTitle = document.getElementById('submenuTitle');
  menuTitle.innerText = ''
  submenu.setAttribute('hidden', 'true');
  submenu.removeAttribute('style');
  while (submenuBody.hasChildNodes()) {
    submenuBody.removeChild(submenuBody.firstChild);
  }
}
function openAddColumn(column) {
  const modal = document.getElementById('modal');
  const modalBody = document.getElementById('modalBody');
  const modalTitle = document.getElementById('modalTitle');
  const modalBodyHTML = `
    <label for="new-col-title">
      <strong>Column name</strong>
    </label>
    <input id="new-col-title" placeholder="Enter a column name (To do, In Progress, Done)" />
    <strong>Automation</strong>
    <p>Choose a preset to enable progress tracking, automation, and better context sharing across your project.</p>
    <button id="choose-tracking">
      <span>Preset: </span><span id="new-col-tracking" data-tracking="none">None</span>
    </button>
    <button disabled="true" id="create-col-btn" class="confirm-btn">Create column</button>
 `;
 modalTitle.innerText = 'Add a Column';
 modalBody.innerHTML = modalBodyHTML;
 openModal();
}
function addColumn(newColTitle, newColTracking) {
  const projectStore = JSON.parse(localStorage.getItem('projectStore'));
  const addColDiv = document.getElementById('add-col-div');
  const newColNumber = parseInt(projectStore.runningColCount) + 1;
  const columnHTML = `
  <div id="stage-${newColNumber}" class="col ${newColTracking}-gradient ${newColTracking}-border" data-track="${newColTracking}" draggable="true">
    <div class="colHeader">
      <div id="total-${newColNumber}" class="total ${newColTracking}-border">0</div><h2 class="col-name">${newColTitle}</h2>
      <button id="addCard-${newColNumber}" class="add-card-btn col-btn" title="Add a card to this column">
        <img src="https://res.cloudinary.com/anthony-dee/image/upload/v1546548847/noun_Plus_869750_no_attribute.svg" alt="Add a card to this column" />
      </button>
      <button id="open-col-menu-${newColNumber}" class="open-col-menu-btn col-btn" title="Open column edit menu">
        <img src="https://res.cloudinary.com/anthony-dee/image/upload/v1546548847/noun_ellipsis_869758_no_attribute.svg" alt="Open column edit menu" />
      </button>
    </div>
    <div id="cards-${newColNumber}" class="cardsContainer" data-track="${newColTracking}">
    </div>
  </div>
  `;
  addColDiv.insertAdjacentHTML('beforebegin', columnHTML)
  closeModal();
  let update = new Project(projectStore.title, projectStore.data, newColNumber);
  localStorage.setItem('projectStore', JSON.stringify(update));
  updateProgress();
}
function openDeleteWarning(column) {
  const colName = document.querySelector('#stage-' + column + ' .col-name').innerText;
  const modalBody = document.getElementById('modalBody');
  const modalTitle = document.getElementById('modalTitle');
  const modalBodyHTML = `
    <p>This action will remove any cards and automation preset associated with the column.</p>
    <button id="delete-col-${column}" class="delete-col-btn">Delete column</button><button id="cancel-modal-action">Cancel</button>
  `;
  modalTitle.innerText = 'Delete ' + colName;
  modalBody.innerHTML = modalBodyHTML;
  closeSubMenu()
  openModal()
}
function openColEdit(column) {
  const colName = document.querySelector('#stage-' + column + ' .col-name').innerText
  const modalTitle = document.getElementById('modalTitle');
  const modalBody = document.getElementById('modalBody');
  let updateColText;
  const modalBodyHTML = `
    <input id="update-col-text-${column}" type="text" placeholder="Enter a column name (To Do, In Progress, Done)" value="${colName}"/>
    <button id="update-col-${column}" class="confirm-btn">Update column</button></div>
  `;
  modalTitle.innerText = 'Edit ' + colName;
  modalBody.innerHTML = modalBodyHTML;
  updateColText = document.getElementById('update-col-text-' + column);
  closeSubMenu();
  openModal();
  updateColText.focus()
}
function openCardEdit(card) {
  let updateCardText;
  const cardText = document.getElementById('card-text-' + card).innerText
  const modalBody = document.getElementById('modalBody');
  const modalTitle = document.getElementById('modalTitle');
  const modalBodyHTML = `
    <textarea id="update-card-text-${card}" rows="6" cols="20">${cardText}</textarea>
    <button id="update-card-${card}" class="update-card-btn confirm-btn">Save card</button>
  `;
  modalTitle.innerText = 'Edit card';
  modalBody.innerHTML = modalBodyHTML;
  updateCardText = document.getElementById('update-card-text-' + card)
  closeSubMenu()
  openModal()
  updateCardText.focus()
}
function updateCardText(card) {
  const thisCardText = document.getElementById('card-text-' + card);
  const cardText = document.getElementById(`update-card-text-${card}`).value;
  thisCardText.innerText = cardText;
  updateProjectData();
  closeModal();
}
function deleteCard(card) {
  let deleteConfirm = confirm('This will remove this card from the project');
  const cardContainer = document.getElementById('cards-' + card);
  let cardToDelete = document.getElementById('card-' + card);
  if (deleteConfirm) {
    cardToDelete.parentNode.removeChild(cardToDelete);
    closeSubMenu();
    updateProgress();
  } else {
    // Do nothing
  }
}
function openModal() {
  const modal = document.getElementById('modal');
  const overlay = document.getElementById('overlay');
  showElement(overlay);
  modal.classList.add('open');
  modal.removeAttribute('hidden');
}
function closeModal () {
  const modal = document.getElementById('modal')
  const modalBody = document.getElementById('modalBody');
  const overlay = document.getElementById('overlay');
  modal.setAttribute('hidden', 'true')
  hideElement(overlay);
  modal.classList.remove('open');
  while (modalBody.hasChildNodes()) {
    modalBody.removeChild(modalBody.firstChild);
  }
}
function showElement(el) {
  el.classList.replace('hidden', 'show');
}
function hideElement(el) {
  el.classList.replace('show', 'hidden');
}
function openAddCardForm(column) {
  const addBtnDiv = document.createElement('div');
  const cardContainer = document.getElementById('cards-' + column);
  const addCardTemplate = `
    <div id="add-card-div-${column}" class="add-card-box">
      <form>
        <textarea id="new-card-text-${column}" class="new-card-text" placeholder="Enter card text" rows="3"></textarea>
        <button id="add-card-${column}" class="confirm-btn flex-btn-left" type="button">Add</button>
        <button type="button" id="remove-add-card-form-${column}" class="flex-btn-right">Cancel</button>
      </form>
    </div>
  `;
  if (!cardContainer.querySelector('.add-card-box')) {
    cardContainer.insertAdjacentHTML('afterbegin', addCardTemplate);
  }
}
function addCard(column){
  const colTracking = document.getElementById('stage-' + column).getAttribute('data-track')
  const textarea = document.getElementById('new-card-text-' + column)
  const newNoteText = textarea.value;
  const allCards = document.querySelectorAll('.card');
  const newCardNo = allCards.length + 1;
  const addCardDiv = document.getElementById('add-card-div-' + column);
  const cardTemplate = `
    <div id="card-${newCardNo}" class="card" draggable="true" data-card-track="${colTracking}">
      <div id="card-text-${newCardNo}" class="card-text">${newNoteText}</div>
      <button id="open-card-menu-${newCardNo}" class="open-card-menu-btn card-btn" title="Open card edit menu">
        <img src="https://res.cloudinary.com/anthony-dee/image/upload/v1546548847/noun_ellipsis_869758_no_attribute.svg" alt="Open card edit menu" />
      </button>
    </div>
  `;
  if (newNoteText === '') {
    alert('Please enter a card description');
  } else {
    textarea.value = '';
    addCardDiv.insertAdjacentHTML('afterend', cardTemplate)
    updateProgress();
  }
}
function closeAddCardForm(column){
  const addBtnDiv = document.getElementById('add-card-div-' + column);
  const cardContainer = document.getElementById('cards-' + column);
  cardContainer.removeChild(addBtnDiv);
}