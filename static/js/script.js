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

// TOAST NOTIFICATIONS
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


// AUTH MODAL FUNCTIONS
function openLogin() {
    const loginModal = document.getElementById("loginModal");
    if (loginModal) {
        loginModal.style.display = "flex";
        document.body.style.overflow = 'hidden';
        
        if (!sessionStorage.getItem('intended_url')) {
            sessionStorage.setItem('intended_url', window.location.pathname);
        }
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


// OTP TIMER
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


// FORM HANDLERS
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
            
            const intendedUrl = sessionStorage.getItem('intended_url');
            
            setTimeout(() => {
                if (intendedUrl && intendedUrl !== '/') {
                    sessionStorage.removeItem('intended_url');
                    window.location.href = intendedUrl;
                } else {
                    sessionStorage.removeItem('intended_url');
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
        
        const intendedUrl = sessionStorage.getItem('intended_url');
        
        setTimeout(() => {
            if (intendedUrl && intendedUrl !== '/') {
                sessionStorage.removeItem('intended_url');
                window.location.href = intendedUrl;
            } else {
                sessionStorage.removeItem('intended_url');
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


// PROTECTED ROUTES HANDLER
function interceptProtectedRoutes() {
    document.addEventListener('click', function(e) {
        let link = e.target.closest('a');
        
        if (!link) return;
        
        const href = link.getAttribute('href');
        const protectedRoutes = ['/dashboard', '/courses', '/notes'];
        
        if (protectedRoutes.includes(href)) {
            e.preventDefault();
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
            window.location.href = targetUrl;
        } else {
            showLoginModalForProtectedRoute(targetUrl);
        }
    })
    .catch(error => {
        console.error('Auth check error:', error);
        showLoginModalForProtectedRoute(targetUrl);
    });
}

function showLoginModalForProtectedRoute(targetUrl) {
    sessionStorage.setItem('intended_url', targetUrl);
    openLogin();
    showToast('Please login to access this feature', 'warning');
}


// DOM CONTENT LOADED
document.addEventListener("DOMContentLoaded", () => {
    interceptProtectedRoutes();

    const showAuth = document.body.dataset.showAuth;
    if (showAuth === 'true') {
        openLogin();
    }

    const loginForm = document.querySelector('.login-face form');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }

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
// COURSE MODULES - GLOBAL VARIABLES
// ========================
let currentCourseId = null;
let completedLectures = {};
let currentNote = {};


// DASHBOARD SECTIONS
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
    currentCourseId = String(courseId);
    
    const moduleTitle = document.getElementById('module-title');
    if (moduleTitle) {
        moduleTitle.textContent = 'Course Modules - ' + (modules[currentCourseId]?.[0]?.name || `Course ${courseId}`);
    }
    
    const accordion = document.getElementById('moduleAccordion');
    if (!accordion) return;
    
    accordion.innerHTML = '';

    if (!modules || !modules[currentCourseId]) {
        console.error('No modules found for course:', currentCourseId);
        showToast('Course modules are being prepared. Please check back soon!', 'info');
        return;
    }

    modules[currentCourseId].forEach((module, idx) => {
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
                                const key = currentCourseId + '-' + module.id + '-' + ch.name;
                                return `
                                    <tr>
                                        <td>${ch.name}</td>
                                        <td class="text-center">
                                            <a href="${ch.youtube}" target="_blank" class="me-2" title="Watch Video">
                                                <svg class="resource-icon" fill="#dc2626" viewBox="0 0 24 24">
                                                    <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                                                </svg>
                                            </a>
                                            <a href="${ch.pdf}" target="_blank" title="Download PDF">
                                                <svg class="resource-icon" fill="#dc2626" viewBox="0 0 24 24">
                                                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm-1 2l5 5h-5V4zM8 18v-1h8v1H8zm0-4v-1h8v1H8zm0-4V9h5v1H8z"/>
                                                </svg>
                                            </a>
                                        </td>
                                        <td class="text-center">
                                            <button class="btn btn-sm btn-primary" onclick="saveLecture('${ch.name}', '${currentCourseId}')">Save</button>
                                        </td>
                                        <td class="text-center">
                                            <button class="btn btn-sm btn-success" onclick="openNotes('${currentCourseId}', '${module.id}', '${ch.name}')">Notes</button>
                                        </td>
                                        <td class="text-center">
                                            <button class="btn btn-sm btn-outline-secondary" id="btn-${key}" onclick="toggleComplete('${key}', '${currentCourseId}')">Mark</button>
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
    
    loadCompletedChapters(parseInt(currentCourseId));
}

function closeModules() {
    const modulesSection = document.getElementById('modules-section');
    if (modulesSection) {
        modulesSection.classList.add('d-none');
    }
    currentCourseId = null;
}


function saveLecture(lectureName, courseId) {
    const actualCourseId = courseId || currentCourseId;
    
    if (!actualCourseId) {
        showToast('Course ID not found', 'error');
        return;
    }

    fetch('/save-lecture', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            course_id: parseInt(actualCourseId),
            lecture_name: lectureName
        })
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
        
        if (d.success) {
            showToast(d.message, 'success');
        } else {
            showToast(d.message || 'Failed to save lecture', 'error');
        }
    })
    .catch(error => {
        showToast('Failed to save lecture. Please try again.', 'error');
        console.error('Save lecture error:', error);
    });
}


function openNotes(courseId, moduleId, chapterName) {
    currentNote = { 
        course: courseId, 
        module: moduleId, 
        chapter: chapterName 
    };
    
    const modalChapter = document.getElementById('modal-chapter');
    if (modalChapter) {
        modalChapter.textContent = `Chapter: ${chapterName}`;
    }
    
    const notesTextarea = document.getElementById('notes-textarea');
    if (notesTextarea) {
        notesTextarea.value = 'Loading...';
        notesTextarea.disabled = true;
    }
    
    fetch('/get-notes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            course_id: parseInt(courseId),
            module_id: moduleId,
            chapter_name: chapterName
        })
    })
    .then(r => r.json())
    .then(d => {
        if (notesTextarea) {
            notesTextarea.disabled = false;
            notesTextarea.value = d.note_text || '';
        }
    })
    .catch(error => {
        console.error('Error loading notes:', error);
        if (notesTextarea) {
            notesTextarea.disabled = false;
            notesTextarea.value = '';
        }
    });
    
    const notesModal = document.getElementById('notesModal');
    if (notesModal && typeof bootstrap !== 'undefined') {
        new bootstrap.Modal(notesModal).show();
    }
}


function saveNotes() {
    const notesTextarea = document.getElementById('notes-textarea');
    if (!notesTextarea) return;
    
    const notesContent = notesTextarea.value;
    
    fetch('/save-notes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            course_id: parseInt(currentNote.course),
            module_id: currentNote.module,
            chapter_name: currentNote.chapter,
            note_text: notesContent
        })
    })
    .then(r => r.json())
    .then(d => {
        if (d.require_login) {
            showToast(d.message, 'warning');
            setTimeout(() => openLogin(), 1000);
            return;
        }
        
        if (d.success) {
            showToast(d.message, 'success');
            
            const notesModal = document.getElementById('notesModal');
            if (notesModal && typeof bootstrap !== 'undefined') {
                const modalInstance = bootstrap.Modal.getInstance(notesModal);
                if (modalInstance) {
                    modalInstance.hide();
                }
            }
        } else {
            showToast(d.message || 'Failed to save notes', 'error');
        }
    })
    .catch(error => {
        showToast('Failed to save notes. Please try again.', 'error');
        console.error('Save notes error:', error);
    });
}


function toggleComplete(chapterKey, courseId) {
    const btn = document.getElementById('btn-' + chapterKey);
    if (!btn) return;
    
    if (completedLectures[chapterKey]) {
        showToast('Chapter already marked as complete', 'info');
        return;
    }
    
    const actualCourseId = courseId || currentCourseId;
    
    if (!actualCourseId) {
        showToast('Course ID not found', 'error');
        return;
    }
    
    btn.disabled = true;
    const originalText = btn.textContent;
    btn.textContent = 'Marking...';
    
    fetch('/mark-complete', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            course_id: parseInt(actualCourseId),
            chapter_key: chapterKey
        })
    })
    .then(r => r.json())
    .then(d => {
        btn.disabled = false;
        
        if (d.require_login) {
            btn.textContent = originalText;
            showToast(d.message, 'warning');
            setTimeout(() => openLogin(), 1000);
            return;
        }
        
        if (d.success) {
            completedLectures[chapterKey] = true;
            
            btn.textContent = '✓ Done';
            btn.className = 'btn btn-sm btn-success';
            
            showToast(d.message, 'success');
            
            setTimeout(() => {
                location.reload();
            }, 1000);
        } else {
            btn.textContent = originalText;
            showToast(d.message || 'Failed to mark chapter complete', 'error');
        }
    })
    .catch(error => {
        btn.disabled = false;
        btn.textContent = originalText;
        showToast('Failed to mark chapter complete. Please try again.', 'error');
        console.error('Mark complete error:', error);
    });
}


function loadCompletedChapters(courseId) {
    fetch('/get-completed-chapters', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ course_id: courseId })
    })
    .then(r => r.json())
    .then(d => {
        if (d.success && d.completed_chapters) {
            d.completed_chapters.forEach(chapterKey => {
                completedLectures[chapterKey] = true;
                
                const btn = document.getElementById('btn-' + chapterKey);
                if (btn) {
                    btn.textContent = '✓ Done';
                    btn.className = 'btn btn-sm btn-success';
                }
            });
        }
    })
    .catch(error => {
        console.error('Error loading completed chapters:', error);
    });
}
