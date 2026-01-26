const texts = [
    "Whatever your demand,<br>you get on <span>Begin2Code</span>."
];

let i = 0;
const el = document.getElementById("mainText");

if (el) {
    setInterval(() => {
        el.style.opacity = 0;
        setTimeout(() => {
            i = (i + 1) % texts.length;
            el.innerHTML = texts[i];
            el.style.opacity = 1;
        }, 500);
    }, 4000);
}

function showToast(message, type = 'info') {
    if (typeof toastr !== "undefined") {
        if (type === 'success') {
            toastr.success(message);
        } else if (type === 'error') {
            toastr.error(message);
        } else if (type === 'warning') {
            toastr.warning(message);
        } else {
            toastr.info(message);
        }
    } else {
        const toast = document.createElement('div');
        toast.className = `custom-toast toast-${type}`;
        toast.innerHTML = `
            <div class="toast-content">
                <span class="toast-icon">${type === 'success' ? '✓' : type === 'error' ? '✕' : 'ℹ'}</span>
                <span class="toast-message">${message}</span>
            </div>
        `;
        
        const styles = `
            position: fixed;
            top: 20px;
            right: 20px;
            min-width: 300px;
            padding: 16px 20px;
            background: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : type === 'warning' ? '#f59e0b' : '#3b82f6'};
            color: white;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 10000;
            animation: slideInRight 0.3s ease-out;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        `;
        
        toast.style.cssText = styles;
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.style.animation = 'slideOutRight 0.3s ease-out';
            setTimeout(() => toast.remove(), 300);
        }, 4000);
    }
}

const toastStyles = document.createElement('style');
toastStyles.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
    
    .toast-content {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .toast-icon {
        font-size: 20px;
        font-weight: bold;
    }
    
    .toast-message {
        flex: 1;
        font-size: 14px;
        line-height: 1.4;
    }
`;
document.head.appendChild(toastStyles);

// ========================
// AUTH MODAL FUNCTIONS
// ========================
function openLogin() {
    const loginModal = document.getElementById("loginModal");
    if (loginModal) {
        loginModal.style.display = "flex";
        document.body.style.overflow = 'hidden';
    }
}

function closeLogin() {
    const loginModal = document.getElementById("loginModal");
    if (loginModal) {
        loginModal.style.display = "none";
    }
    document.body.style.overflow = 'auto';

    const card = document.getElementById("loginCard");
    if (card) {
        card.classList.remove("flip");
    }

    const registerContent = document.getElementById("registerContent");
    const verifyContent = document.getElementById("verifyContent");

    if (registerContent) {
        registerContent.classList.remove("hidden");
        registerContent.classList.add("active");
    }

    if (verifyContent) {
        verifyContent.classList.remove("active");
        verifyContent.classList.add("hidden");
    }
}

function flipAuth() {
    const card = document.getElementById("loginCard");
    if (card) {
        card.classList.toggle("flip");
    }
}

function showVerification() {
    const register = document.getElementById("registerContent");
    const verify = document.getElementById("verifyContent");

    if (register) {
        register.classList.remove("active");
        register.classList.add("hidden");
    }

    if (verify) {
        verify.classList.remove("hidden");
        verify.classList.add("active");
    }

    startTimer(180);
}

// ========================
// OTP TIMER
// ========================
let timerInterval;
function startTimer(seconds) {
    const timerEl = document.getElementById("timer");
    if (!timerEl) return;
    
    let timeLeft = seconds;

    if (timerInterval) {
        clearInterval(timerInterval);
    }

    timerInterval = setInterval(() => {
        let min = Math.floor(timeLeft / 60);
        let sec = timeLeft % 60;

        timerEl.textContent = String(min).padStart(2, '0') + ":" + String(sec).padStart(2, '0');

        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            timerEl.textContent = "Expired";
            showToast('OTP expired. Please register again.', 'error');
            
            setTimeout(() => {
                const registerContent = document.getElementById("registerContent");
                const verifyContent = document.getElementById("verifyContent");

                if (verifyContent) {
                    verifyContent.classList.remove("active");
                    verifyContent.classList.add("hidden");
                }

                if (registerContent) {
                    registerContent.classList.remove("hidden");
                    registerContent.classList.add("active");
                }
            }, 2000);
        }

        timeLeft--;
    }, 1000);
}

function collectOTP() {
    const inputs = document.querySelectorAll(".otp-box input");
    let otp = "";
    inputs.forEach(input => otp += input.value);
    return otp;
}

// ========================
// FORM HANDLERS
// ========================
function handleRegister(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const submitBtn = form.querySelector('button[type="submit"]');
    
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';
    }

    fetch('/register', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Register';
        }
        
        if (data.success) {
            showToast(data.message, 'success');
            setTimeout(() => {
                showVerification();
            }, 500);
        } else {
            showToast(data.message, 'error');
        }
    })
    .catch(error => {
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Register';
        }
        showToast('Failed to connect to server. Please check your connection.', 'error');
        console.error('Registration error:', error);
    });
}

function handleVerifyOTP(event) {
    event.preventDefault();

    const otp = collectOTP();
    
    if (otp.length !== 6) {
        showToast('Please enter complete 6-digit OTP', 'warning');
        return;
    }

    const formData = new FormData();
    formData.append('otp', otp);
    
    const submitBtn = event.target.querySelector('button[type="submit"]');
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Verifying...';
    }

    fetch('/verify-otp', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Verify';
        }
        
        if (data.success) {
            showToast(data.message, 'success');
            
            // Check if there's an intended URL
            const intendedUrl = sessionStorage.getItem('intended_url');
            
            setTimeout(() => {
                if (intendedUrl) {
                    sessionStorage.removeItem('intended_url');
                    window.location.href = intendedUrl;
                } else {
                    window.location.href = data.redirect || '/dashboard';
                }
            }, 1500);
        } else {
            showToast(data.message, 'error');

            if (data.session_expired) {
                setTimeout(() => {
                    const registerContent = document.getElementById("registerContent");
                    const verifyContent = document.getElementById("verifyContent");

                    if (verifyContent) {
                        verifyContent.classList.remove("active");
                        verifyContent.classList.add("hidden");
                    }

                    if (registerContent) {
                        registerContent.classList.remove("hidden");
                        registerContent.classList.add("active");
                    }
                }, 2000);
            } else {
                const inputs = document.querySelectorAll(".otp-box input");
                inputs.forEach(input => input.value = '');
                if (inputs[0]) inputs[0].focus();
            }
        }
    })
    .catch(error => {
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Verify';
        }
        showToast('Failed to connect to server. Please check your connection.', 'error');
        console.error('OTP verification error:', error);
    });
}

function handleLogin(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const submitBtn = form.querySelector('button[type="submit"]');
    
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Signing in...';
    }

    fetch('/login', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Sign In';
        }
        
        if (data.success) {
            showToast('Login successful! Redirecting...', 'success');
            
            // Check if there's an intended URL (where user wanted to go)
            const intendedUrl = sessionStorage.getItem('intended_url');
            
            setTimeout(() => {
                if (intendedUrl) {
                    // Clear the stored URL
                    sessionStorage.removeItem('intended_url');
                    // Redirect to intended page
                    window.location.href = intendedUrl;
                } else {
                    // Default redirect from server
                    window.location.href = data.redirect || '/dashboard';
                }
            }, 1000);
        } else {
            showToast(data.message, 'error');
        }
    })
    .catch(error => {
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = 'Sign In';
        }
        showToast('Failed to connect to server. Please check your connection.', 'error');
        console.error('Login error:', error);
    });
}

// ========================
// PROTECTED ROUTES HANDLER (PROFESSIONAL APPROACH)
// ========================
function interceptProtectedRoutes() {
    // Listen to all clicks on the document
    document.addEventListener('click', function(e) {
        // Check if clicked element is a link or inside a link
        let link = e.target.closest('a');
        
        if (!link) return;
        
        const href = link.getAttribute('href');
        
        // List of protected routes
        const protectedRoutes = ['/dashboard', '/courses', '/notes'];
        
        // Check if this is a protected route
        if (protectedRoutes.includes(href)) {
            e.preventDefault(); // Stop normal navigation
            
            // Check authentication status
            checkAuthAndNavigate(href);
        }
    });
}

function checkAuthAndNavigate(targetUrl) {
    fetch('/check-auth', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.authenticated) {
            // User is logged in - navigate normally
            window.location.href = targetUrl;
        } else {
            // User not logged in - show modal
            showLoginModalForProtectedRoute(targetUrl);
        }
    })
    .catch(error => {
        console.error('Auth check error:', error);
        // On error, show login modal to be safe
        showLoginModalForProtectedRoute(targetUrl);
    });
}

function showLoginModalForProtectedRoute(targetUrl) {
    // Save where user wanted to go
    sessionStorage.setItem('intended_url', targetUrl);
    
    // Show the login modal
    openLogin();
    
    // Show informative message
    showToast('Please login to access this feature', 'warning');
}

// ========================
// DOM CONTENT LOADED
// ========================
document.addEventListener("DOMContentLoaded", () => {
    // Initialize protected routes interceptor
    interceptProtectedRoutes();

    // Check if we need to show auth modal
    const showAuth = document.body.dataset.showAuth;
    if (showAuth === 'true') {
        openLogin();
    }

    // Attach login form handler
    const loginForm = document.querySelector('.login-face form');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }

    // OTP input handlers
    const otpInputs = document.querySelectorAll(".otp-box input");

    otpInputs.forEach((input, index) => {
        input.addEventListener("input", (e) => {
            const value = e.target.value;
            if (value && !/^\d$/.test(value)) {
                e.target.value = '';
                return;
            }
            
            if (value.length === 1 && index < otpInputs.length - 1) {
                otpInputs[index + 1].focus();
            }
        });

        input.addEventListener("keydown", (e) => {
            if (e.key === "Backspace" && e.target.value === "" && index > 0) {
                otpInputs[index - 1].focus();
            }
        });
        
        input.addEventListener("paste", (e) => {
            e.preventDefault();
            const pastedData = e.clipboardData.getData('text').replace(/\D/g, '');
            
            if (pastedData.length === 6) {
                otpInputs.forEach((inp, idx) => {
                    inp.value = pastedData[idx] || '';
                });
                otpInputs[5].focus();
            }
        });
    });

    // Configure toastr if available
    if (typeof toastr !== "undefined") {
        toastr.options = {
            closeButton: true,
            progressBar: true,
            positionClass: "toast-top-right",
            timeOut: 4000,
            extendedTimeOut: 1000,
            showEasing: 'swing',
            hideEasing: 'linear',
            showMethod: 'fadeIn',
            hideMethod: 'fadeOut'
        };
    }
});

// ========================
// COURSE MODULES
// ========================
// modules variable is loaded from dashboard.html template
let completedLectures = {};
let savedNotes = {};
let currentNote = {};

function showSection(section, el) {
    document.querySelectorAll('.content-section').forEach(s => s.classList.add('d-none'));
    const sectionEl = document.getElementById(section + '-section');
    if (sectionEl) {
        sectionEl.classList.remove('d-none');
    }
    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
    if (el) el.classList.add('active');
}

function buyCourse(courseId, courseName, coursePrice) {
    if (confirm(`Purchase ${courseName} for ${coursePrice} coins?`)) {
        fetch('/buy-course', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ course_id: courseId })
        })
        .then(r => {
            if (!r.ok) throw new Error('Network error');
            return r.json();
        })
        .then(d => {
            if (d.require_login) {
                showToast(d.message, 'warning');
                setTimeout(() => openLogin(), 1000);
                return;
            }
            
            if (d.low_balance) {
                showToast(d.message, 'error');
                return;
            }
            
            showToast(d.message, d.success ? 'success' : 'error');
            if (d.success) {
                updateCoinsDisplay(d.remaining_coins);
                setTimeout(() => location.reload(), 1500);
            }
        })
        .catch(error => {
            showToast('Failed to process purchase. Please try again.', 'error');
            console.error('Purchase error:', error);
        });
    }
}

function updateCoinsDisplay(coins) {
    const coinsElement = document.getElementById('userCoins');
    if (coinsElement) {
        coinsElement.textContent = coins;
    }
}

function startLearning(courseId) {
    // Convert courseId to string for dictionary lookup
    const courseIdStr = String(courseId);
    
    const moduleTitle = document.getElementById('module-title');
    if (moduleTitle) {
        moduleTitle.textContent = 'Course Modules - Course ID: ' + courseIdStr;
    }
    
    const accordion = document.getElementById('moduleAccordion');
    if (!accordion) return;
    
    accordion.innerHTML = '';

    // Check if modules exist for this course
    if (!modules || !modules[courseIdStr]) {
        console.error('No modules found for course:', courseIdStr);
        console.log('Available modules:', Object.keys(modules || {}));
        showToast('Course modules are being prepared. Please check back soon!', 'info');
        return;
    }
    
    console.log('Loading modules for course:', courseIdStr);

    modules[courseIdStr].forEach((module, idx) => {
        const collapseId = `collapse${idx}`;
        let content = '';

        if (module.available) {
            content = `
                <div class="table-responsive">
                    <table class="table table-hover mb-0">
                        <thead class="table-light">
                            <tr>
                                <th>Chapter Name</th>
                                <th class="text-center">Resources</th>
                                <th class="text-center">Save Lecture</th>
                                <th class="text-center">Notes</th>
                                <th class="text-center">Complete</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${module.chapters.map(ch => {
                                const key = courseIdStr + '-' + module.id + '-' + ch.name;
                                return `
                                    <tr>
                                        <td>${ch.name}</td>
                                        <td class="text-center">
                                            <a href="${ch.youtube}" target="_blank" class="me-2">
                                                <svg class="resource-icon" fill="#dc2626" viewBox="0 0 24 24" style="width:24px;height:24px;">
                                                    <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                                                </svg>
                                            </a>
                                            <a href="${ch.pdf}" target="_blank">
                                                <svg class="resource-icon" fill="#dc2626" viewBox="0 0 24 24" style="width:24px;height:24px;">
                                                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm-1 2l5 5h-5V4zM8 18v-1h8v1H8zm0-4v-1h8v1H8zm0-4V9h5v1H8z"/>
                                                </svg>
                                            </a>
                                        </td>
                                        <td class="text-center">
                                            <button class="btn btn-sm btn-primary" onclick="saveLecture('${ch.name}')">Save</button>
                                        </td>
                                        <td class="text-center">
                                            <button class="btn btn-sm btn-success" onclick="openNotes('${courseIdStr}', '${module.id}', '${ch.name}')">Notes</button>
                                        </td>
                                        <td class="text-center">
                                            <button class="btn btn-sm btn-outline-secondary" id="btn-${key}" onclick="toggleComplete('${key}')">Mark</button>
                                        </td>
                                    </tr>
                                `;
                            }).join('')}
                        </tbody>
                    </table>
                </div>
            `;
        } else {
            content = `
                <div class="coming-soon text-center py-4">
                    <i class="fa fa-clock fs-1 text-muted mb-3"></i>
                    <p class="mb-2 fw-bold">📚 Content Coming Soon!</p>
                    <small class="text-muted">This module will be available in the next update. Keep learning!</small>
                </div>
            `;
        }

        accordion.innerHTML += `
            <div class="accordion-item">
                <h2 class="accordion-header">
                    <button class="accordion-button ${idx !== 0 ? 'collapsed' : ''}" type="button" data-bs-toggle="collapse" data-bs-target="#${collapseId}">
                        ${module.name}
                    </button>
                </h2>
                <div id="${collapseId}" class="accordion-collapse collapse ${idx === 0 ? 'show' : ''}" data-bs-parent="#moduleAccordion">
                    <div class="accordion-body">${content}</div>
                </div>
            </div>
        `;
    });

    const modulesSection = document.getElementById('modules-section');
    if (modulesSection) {
        modulesSection.classList.remove('d-none');
    }
}

function closeModules() {
    const modulesSection = document.getElementById('modules-section');
    if (modulesSection) {
        modulesSection.classList.add('d-none');
    }
}

function toggleComplete(key) {
    const btn = document.getElementById('btn-' + key);
    if (!btn) return;
    
    completedLectures[key] = !completedLectures[key];
    btn.textContent = completedLectures[key] ? '✓ Done' : 'Mark';
    btn.className = completedLectures[key] ? 'btn btn-sm btn-success' : 'btn btn-sm btn-outline-secondary';
    
    if (completedLectures[key]) {
        showToast('Chapter marked as complete!', 'success');
    }
}

function saveLecture(name) {
    showToast('Lecture saved: ' + name, 'success');
}

function openNotes(course, module, chapter) {
    currentNote = { course, module, chapter };
    
    const modalChapter = document.getElementById('modal-chapter');
    if (modalChapter) {
        modalChapter.textContent = 'Chapter: ' + chapter;
    }
    
    const key = course + '-' + module + '-' + chapter;
    const notesTextarea = document.getElementById('notes-textarea');
    if (notesTextarea) {
        notesTextarea.value = savedNotes[key] || '';
    }
    
    const notesModal = document.getElementById('notesModal');
    if (notesModal && typeof bootstrap !== 'undefined') {
        new bootstrap.Modal(notesModal).show();
    }
}

function saveNotes() {
    const key = currentNote.course + '-' + currentNote.module + '-' + currentNote.chapter;
    const notesTextarea = document.getElementById('notes-textarea');
    if (notesTextarea) {
        savedNotes[key] = notesTextarea.value;
    }
    
    const notesModal = document.getElementById('notesModal');
    if (notesModal && typeof bootstrap !== 'undefined') {
        bootstrap.Modal.getInstance(notesModal).hide();
    }
    
    showToast('Notes saved successfully!', 'success');
}