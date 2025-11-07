// app.js

// Turabanza dushakisha button dukoresheje ID twarayihaye muri HTML
const learnMoreBtn = document.getElementById('learn-more-btn');

// Turashyiraho 'Event Listener' (Kuvuga ngo: 'Iyo bayikanze, kora ibi')
learnMoreBtn.addEventListener('click', function() {
    
    // Iki gice ni cyo kizakora iyo umuntu yikanze button
    
    // Tugira message nshya
    const newMessage = "Murakoze kunyikana! Ubu murabizi.";
    
    // Duhindura inyandiko iri kuri button
    learnMoreBtn.textContent = newMessage;
    
    // Dushobora no guhindura ibara ryayo (byo muri CSS)
    learnMoreBtn.style.backgroundColor = '#ffc107'; // Umukundo
    
    // Dushobora no kuvana buttonho umusogongero w'akanya gato (animation)
    setTimeout(() => {
        alert("Wafunguye ubumenyi bushya!");
    }, 100);
});

console.log("JavaScript yageze mu Rubuga Rwiza!");

// app.js (ONGERAHO IBI BICE)

// ------------------------------------------------
// Code yo Gukora Popup/Modal y'Amasaha
// ------------------------------------------------

const selectTimeBtn = document.getElementById('select-time-btn');
const timeDisplay = document.getElementById('time-display');
const selectedTimeInput = document.getElementById('selected-time');

// 1. Gukora Popup (Modal) y'Amasaha mu buryo bwa HTML (JavaScript ifata uruhare)
const createTimeModal = () => {
    // Turakora Modal/Popup mu buryo bwa Dynamic
    const modal = document.createElement('div');
    modal.className = 'time-modal';
    modal.innerHTML = `
        <div class="modal-content">
            <h3>Tora Isaha (06:00 - 21:00)</h3>
            <div class="time-slots-container">
                </div>
            <button class="close-modal-btn">Funga</button>
        </div>
    `;
    document.body.appendChild(modal);
    return modal;
};

// 2. Gukora Amasaha (Slots)
const createTimeSlots = (container) => {
    // Gusaba amasaha kuva 6 kugeza 21 (kuva 6AM kugeza 9PM)
    for (let hour = 6; hour <= 21; hour++) {
        // Twagabanyamo kabiri buri saha (e.g., 06:00 na 06:30)
        [0, 30].forEach(minute => {
            const time = `${hour < 10 ? '0' + hour : hour}:${minute === 0 ? '00' : minute}`;
            const slot = document.createElement('button');
            slot.textContent = time;
            slot.className = 'time-slot-btn';
            
            // Iyo umukiriya akandazeho
            slot.addEventListener('click', () => {
                // Kwandika isaha yatoranyijwe mu field ya Hidden
                selectedTimeInput.value = time; 
                timeDisplay.textContent = `Isaha yatoranyijwe: **${time}**`;
                document.querySelector('.time-modal').remove(); // Kufunga Modal
            });
            container.appendChild(slot);
        });
    }
};

// 3. Iyo Button 'Tora Isaha' ikanzwe
selectTimeBtn.addEventListener('click', () => {
    const modal = createTimeModal();
    const slotsContainer = modal.querySelector('.time-slots-container');
    createTimeSlots(slotsContainer);

    // Kugira ngo ifunge iyo umuntu yikanze hanze cyangwa kuri button 'Funga'
    modal.addEventListener('click', (e) => {
        if (e.target.classList.contains('time-modal') || e.target.classList.contains('close-modal-btn')) {
            modal.remove();
        }
    });
});

// Twibagiwe CSS yo kuri modal (Uzasaba ko tugushyiriramo nyuma)