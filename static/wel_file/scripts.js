// Get elements
const loginBtn = document.querySelector('.login-btn');
const signupBtn = document.querySelector('.signup-btn');
const loginModal = document.getElementById('loginModal');
const closeModal = document.getElementById('closeModal');

// Open login modal
loginBtn.addEventListener('click', () => {
    loginModal.style.display = 'block';
    document.body.classList.add('modal-open');
});

// Close login modal
closeModal.addEventListener('click', () => {
    loginModal.style.display = 'none';
    document.body.classList.remove('modal-open');
});

// Close modal when clicking outside of it
window.addEventListener('click', (event) => {
    if (event.target === loginModal) {
        loginModal.style.display = 'none';
        document.body.classList.remove('modal-open');
    }
});