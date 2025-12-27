/**=================================== Course ================================================ */
const courseModal = document.getElementById('courseModal');

if (courseModal) {
    courseModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;
        const title = button.getAttribute('data-title');
        const coins = button.getAttribute('data-coins'); 
        const originalCoins = Math.round(coins * 1.2);

        courseModal.querySelector('.modal-title').textContent = title;

        courseModal.querySelector('.modal-body').innerHTML = `
          <div class="course-grid">
            <div class="feature-section">

                <div class="feature-item d-flex justify-content-between align-items-start">
                    <div>
                        <div class="feature-header">
                            <h5 class="m-0">Lectures</h5>
                            <span class="badge-blue">SELF PACED</span>
                        </div>
                        <ul class="text-muted small">
                            <li>Recorded sessions provided for all classes</li>
                            <li>Divided Modules Structure for ${title}</li>
                        </ul>
                    </div>
                    <img src="images/M1.png" alt="icon" style="width: 80px;">
                </div>
                
                <div class="feature-item d-flex justify-content-between align-items-start">
                    <div>
                        <div class="feature-header">
                            <h5 class="m-0">Curriculum</h5>
                            <span class="badge-blue">Latest 2026</span>
                        </div>
                        <ul class="text-muted small">
                            <li>Hands-on coding with ${title}</li>
                            <li>Basic to Advance Topics Covered</li>
                        </ul>
                    </div>
                    <img src="images/M2.png" alt="icon" style="width: 80px;">
                </div>

                <div class="feature-item d-flex justify-content-between align-items-start">
                    <div>
                        <div class="feature-header">
                            <h5 class="m-0">Doubt Solving</h5>
                            <span class="badge-blue">24*7</span>
                        </div>
                        <ul class="text-muted small">
                            <li>Instant support on Telegram</li>
                            <li>Weekly live Q&A sessions</li>
                        </ul>
                    </div>
                    <img src="images/M3.png" alt="icon" style="width: 80px;">
                </div>

                <div class="feature-item d-flex justify-content-between align-items-start">
                    <div>
                        <div class="feature-header">
                            <h5 class="m-0">Certifications</h5>
                            <span class="badge-blue">APPROVED</span>
                        </div>
                        <ul class="text-muted small">
                            <li>Enhance your Resume with Approved Certificates</li>
                        </ul>
                    </div>
                    <img src="images/M4.png" alt="icon" style="width: 80px;">
                </div>
            </div>

            <div class="pricing-card">
                <div class="early-bird-header">EARLY BIRD OFFER</div>
                <div class="card-content">
                    <p class="small fw-bold mb-1">LANGUAGES</p>
                    <div class="select-box mb-3">Hindi</div>
                    <div class="select-box mb-3">Hinglish (Hindi + English)</div>
                    
                    <p class="small fw-bold mb-1">BATCH TYPE</p>
                    <div class="select-box mb-3">Self Paced</div>

                    <p class="small fw-bold mb-1">Course Duration</p>
                    <div class="select-box mb-3">4+ Months</div>

                    <div class="mt-4 pt-3 border-top">
                        <p class="mb-0 small text-muted">Course Fee</p>
                        <div class="d-flex align-items-center gap-2">
                            <span class="text-decoration-line-through text-muted small">🪙 ${originalCoins}</span>
                            <span class="badge bg-success" style="font-size: 0.7rem;">15% OFF</span>
                        </div>
                        <div class="coin-display">
                            <span class="coin-icon">🪙</span>${coins}
                        </div>
                    </div>
                    <button class="btn btn-primary w-100 mt-3 py-2 fw-bold">Enroll Now</button>
                </div>
            </div>
          </div>
        `;
    });
}