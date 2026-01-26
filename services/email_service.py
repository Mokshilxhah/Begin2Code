from flask_mail import Message

def send_verification_email(mail, recipient_email, otp):
    msg = Message(
        subject="Begin2Code - Email Verification Code",
        recipients=[recipient_email]
    )

    msg.html = f"""
    <!DOCTYPE html>
    <html>
    <body style="font-family:Arial, sans-serif; background:#f4f6f8; padding:20px;">
        <div style="max-width:500px; margin:auto; background:#ffffff; padding:30px; border-radius:12px;">
            <h2 style="color:#0d6efd;">Verify your email</h2>
            <p>Welcome to <strong>Begin2Code</strong> 👋</p>
            <p>Your verification code is:</p>

            <h1 style="letter-spacing:6px; text-align:center; color:#000; background:#f0f0f0; padding:15px; border-radius:8px;">
                {otp}
            </h1>

            <p style="font-size:14px; color:#555;">
                This code is valid for 3 minutes.  
                If you did not request this, please ignore this email.
            </p>

            <p>— Team Begin2Code</p>
        </div>
    </body>
    </html>
    """

    mail.send(msg)

def send_welcome_email(mail, recipient_email, name):
    msg = Message(
        subject="Welcome to Begin2Code — Your Learning Journey Starts Here",
        recipients=[recipient_email]
    )

    msg.html = f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0; padding:0; background:#eef1f5; font-family:Segoe UI, Roboto, Arial, sans-serif;">
        <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
                <td align="center" style="padding:30px 10px;">

                    <!-- Main Card -->
                    <table width="600" cellpadding="0" cellspacing="0"
                        style="background:#ffffff; border-radius:14px; box-shadow:0 12px 30px rgba(0,0,0,0.08); overflow:hidden;">

                        <!-- Gradient Header -->
                        <tr>
                            <td style="padding:28px; text-align:center;
                                background:linear-gradient(135deg, #0d6efd, #6610f2);
                                color:#ffffff;">
                                <h1 style="margin:0; font-size:30px;">Begin2Code</h1>
                                <p style="margin:8px 0 0; font-size:15px; opacity:0.9;">
                                    Build skills. One line of code at a time.
                                </p>
                            </td>
                        </tr>

                        <!-- Body -->
                        <tr>
                            <td style="padding:35px; color:#2c2f33;">
                                <h2 style="margin-top:0;">Welcome, {name} 👋</h2>

                                <p style="font-size:15px; line-height:1.7;">
                                    We're excited to have you on board with <strong>Begin2Code</strong>.
                                    Your account has been successfully created and you now have access to
                                    structured courses, curated notes, and practical learning resources.
                                </p>

                                <!-- Bonus Coins Box -->
                                <table width="100%" cellpadding="0" cellspacing="0"
                                    style="background:#fef3c7; border-left:4px solid #f59e0b; border-radius:10px; margin:25px 0;">
                                    <tr>
                                        <td style="padding:20px; text-align:center;">
                                            <h3 style="margin-top:0; color:#d97706;">🎉 Welcome Bonus!</h3>
                                            <p style="font-size:18px; margin:10px 0; color:#92400e;">
                                                You've received <strong style="font-size:24px; color:#f59e0b;">5000 Coins</strong>
                                            </p>
                                            <p style="font-size:14px; color:#78350f; margin:5px 0;">
                                                Use these coins to purchase courses and start learning!
                                            </p>
                                        </td>
                                    </tr>
                                </table>

                                <!-- Feature Box -->
                                <table width="100%" cellpadding="0" cellspacing="0"
                                    style="background:#f8f9fb; border-radius:10px; margin:25px 0;">
                                    <tr>
                                        <td style="padding:20px;">
                                            <h3 style="margin-top:0; color:#0d6efd;">What you get</h3>
                                            <ul style="padding-left:20px; line-height:1.8; margin:0;">
                                                <li>Explore Beginner to Advanced courses</li>
                                                <li>Access high-quality Notes & Lectures</li>
                                                <li>Track your learning progress</li>
                                                <li>Purchase courses with your coins</li>
                                            </ul>
                                        </td>
                                    </tr>
                                </table>

                                <!-- Upcoming Box -->
                                <table width="100%" cellpadding="0" cellspacing="0"
                                    style="background:#f8f9fb; border-radius:10px; margin:25px 0;">
                                    <tr>
                                        <td style="padding:20px;">
                                            <h3 style="margin-top:0; color:#0d6efd;">Upcoming Features 🚀</h3>
                                            <ul style="padding-left:20px; line-height:1.8; margin:0;">
                                                <li>Data Structures & Algorithms (DSA)</li>
                                                <li>Advanced Programming Concepts</li>
                                                <li>Interactive Learning Modules</li>
                                                <li>and Many more!</li>
                                            </ul>
                                        </td>
                                    </tr>
                                </table>

                                <!-- CTA Button -->
                                <div style="text-align:center; margin:35px 0;">
                                    <a href="https://begin2code.onrender.com/courses"
                                       style="background:#0d6efd; color:#ffffff;
                                       text-decoration:none; padding:14px 34px;
                                       border-radius:30px; font-size:15px;
                                       display:inline-block;">
                                        Explore Courses →
                                    </a>
                                </div>

                                <p style="font-size:14px; color:#6c757d; line-height:1.6;">
                                    If you did not create this account, please ignore this email
                                    or contact our support team.
                                </p>

                                <p style="margin-bottom:0;">
                                    Happy learning,<br>
                                    <strong>Team Begin2Code</strong>
                                </p>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td style="background:#f1f3f5; padding:18px; text-align:center;
                                font-size:12px; color:#6c757d;">
                                © 2026 Begin2Code · All rights reserved
                            </td>
                        </tr>

                    </table>

                </td>
            </tr>
        </table>
    </body>
    </html>
    """
    
    mail.send(msg)

def send_course_purchase_email(mail, recipient_email, name, course_name, course_price):
    msg = Message(
        subject=f"Course Purchased Successfully - {course_name}",
        recipients=[recipient_email]
    )

    msg.html = f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0; padding:0; background:#eef1f5; font-family:Segoe UI, Roboto, Arial, sans-serif;">
        <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
                <td align="center" style="padding:30px 10px;">

                    <!-- Main Card -->
                    <table width="600" cellpadding="0" cellspacing="0"
                        style="background:#ffffff; border-radius:14px; box-shadow:0 12px 30px rgba(0,0,0,0.08); overflow:hidden;">

                        <!-- Gradient Header -->
                        <tr>
                            <td style="padding:28px; text-align:center;
                                background:linear-gradient(135deg, #10b981, #059669);
                                color:#ffffff;">
                                <h1 style="margin:0; font-size:30px;">🎉 Purchase Confirmed!</h1>
                                <p style="margin:8px 0 0; font-size:15px; opacity:0.9;">
                                    Your learning journey begins now
                                </p>
                            </td>
                        </tr>

                        <!-- Body -->
                        <tr>
                            <td style="padding:35px; color:#2c2f33;">
                                <h2 style="margin-top:0;">Congratulations, {name}! 🎓</h2>

                                <p style="font-size:15px; line-height:1.7;">
                                    Thank you for enrolling in <strong>{course_name}</strong>.
                                    Your payment has been successfully processed and you now have
                                    full access to all course materials, lectures, and resources.
                                </p>

                                <!-- Course Details Box -->
                                <table width="100%" cellpadding="0" cellspacing="0"
                                    style="background:#f0fdf4; border-left:4px solid #10b981; border-radius:10px; margin:25px 0;">
                                    <tr>
                                        <td style="padding:20px;">
                                            <h3 style="margin-top:0; color:#059669;">Course Details</h3>
                                            <table width="100%" style="font-size:15px; line-height:1.8;">
                                                <tr>
                                                    <td style="color:#6b7280; width:40%;">Course Name:</td>
                                                    <td style="font-weight:600;">{course_name}</td>
                                                </tr>
                                                <tr>
                                                    <td style="color:#6b7280;">Coins Spent:</td>
                                                    <td style="font-weight:600; color:#10b981;">{course_price} Coins</td>
                                                </tr>
                                                <tr>
                                                    <td style="color:#6b7280;">Access:</td>
                                                    <td style="font-weight:600;">Lifetime</td>
                                                </tr>
                                                <tr>
                                                    <td style="color:#6b7280;">Status:</td>
                                                    <td style="font-weight:600; color:#10b981;">✓ Active</td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>

                                <!-- What's Included Box -->
                                <table width="100%" cellpadding="0" cellspacing="0"
                                    style="background:#f8f9fb; border-radius:10px; margin:25px 0;">
                                    <tr>
                                        <td style="padding:20px;">
                                            <h3 style="margin-top:0; color:#0d6efd;">What's Included 📦</h3>
                                            <ul style="padding-left:20px; line-height:1.8; margin:0;">
                                                <li>Complete video lectures & tutorials</li>
                                                <li>Downloadable notes & resources</li>
                                                <li>Hands-on projects & assignments</li>
                                                <li>24/7 access to course materials</li>
                                                <li>Certificate of completion</li>
                                            </ul>
                                        </td>
                                    </tr>
                                </table>

                                <!-- Next Steps Box -->
                                <table width="100%" cellpadding="0" cellspacing="0"
                                    style="background:#fef3c7; border-left:4px solid #f59e0b; border-radius:10px; margin:25px 0;">
                                    <tr>
                                        <td style="padding:20px;">
                                            <h3 style="margin-top:0; color:#d97706;">Next Steps 🚀</h3>
                                            <ol style="padding-left:20px; line-height:1.8; margin:0;">
                                                <li>Visit your <strong>Dashboard</strong> to access the course</li>
                                                <li>Start with the <strong>Fundamentals</strong> module</li>
                                                <li>Track your progress as you learn</li>
                                                <li>Join our community for support</li>
                                            </ol>
                                        </td>
                                    </tr>
                                </table>

                                <!-- CTA Button -->
                                <div style="text-align:center; margin:35px 0;">
                                    <a href="https://begin2code.onrender.com/dashboard"
                                       style="background:#10b981; color:#ffffff;
                                       text-decoration:none; padding:14px 34px;
                                       border-radius:30px; font-size:15px;
                                       display:inline-block; font-weight:600;">
                                        Start Learning Now →
                                    </a>
                                </div>

                                <p style="font-size:14px; color:#6c757d; line-height:1.6; 
                                    background:#f8f9fb; padding:15px; border-radius:8px;">
                                    💡 <strong>Pro Tip:</strong> Make the most of your learning by setting aside 
                                    dedicated time each day. Consistency is key to mastering new skills!
                                </p>

                                <p style="font-size:14px; color:#6c757d; line-height:1.6; margin-top:25px;">
                                    Need help? Our support team is here for you. Simply reply to this email
                                    or visit our help center.
                                </p>

                                <p style="margin-bottom:0;">
                                    Happy coding,<br>
                                    <strong>Team Begin2Code</strong>
                                </p>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td style="background:#f1f3f5; padding:18px; text-align:center;
                                font-size:12px; color:#6c757d;">
                                © 2026 Begin2Code · All rights reserved<br>
                                <span style="font-size:11px;">This is a confirmation email for your course purchase</span>
                            </td>
                        </tr>

                    </table>

                </td>
            </tr>
        </table>
    </body>
    </html>
    """
    
    mail.send(msg)

def forgot_password(mail, recipient_email, name):
    msg = Message(
        subject="Your Begin2Code Password Was Changed 🔐",
        recipients=[recipient_email]
    )

    msg.html = f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0; padding:0; background:#eef1f5; font-family:Segoe UI, Roboto, Arial, sans-serif;">
        <table width="100%" cellpadding="0" cellspacing="0">
            <tr>
                <td align="center" style="padding:30px 10px;">

                    <table width="600" cellpadding="0" cellspacing="0"
                        style="background:#ffffff; border-radius:14px;
                        box-shadow:0 12px 30px rgba(0,0,0,0.08); overflow:hidden;">

                        <!-- Header -->
                        <tr>
                            <td style="padding:28px; text-align:center;
                                background:linear-gradient(135deg, #ef4444, #dc2626);
                                color:#ffffff;">
                                <h1 style="margin:0; font-size:30px;">🔐 Password Updated</h1>
                                <p style="margin:8px 0 0; font-size:15px; opacity:0.95;">
                                    Security confirmation
                                </p>
                            </td>
                        </tr>

                        <!-- Body -->
                        <tr>
                            <td style="padding:35px; color:#2c2f33;">
                                <h2 style="margin-top:0;">Hello {name},</h2>

                                <p style="font-size:15px; line-height:1.7;">
                                    This is a confirmation that your <strong>Begin2Code</strong>
                                    account password was successfully changed.
                                </p>

                                <!-- Info Box -->
                                <table width="100%" cellpadding="0" cellspacing="0"
                                    style="background:#fef2f2; border-left:4px solid #ef4444;
                                    border-radius:10px; margin:25px 0;">
                                    <tr>
                                        <td style="padding:20px;">
                                            <p style="margin:0; font-size:14px; color:#7f1d1d;">
                                                ⚠ If you did not make this change, please reset your password
                                                immediately and contact our support team.
                                            </p>
                                        </td>
                                    </tr>
                                </table>

                                <!-- Security Tips -->
                                <table width="100%" cellpadding="0" cellspacing="0"
                                    style="background:#f8f9fb; border-radius:10px; margin:25px 0;">
                                    <tr>
                                        <td style="padding:20px;">
                                            <h3 style="margin-top:0; color:#0d6efd;">Security Tips 🔒</h3>
                                            <ul style="padding-left:20px; line-height:1.8; margin:0;">
                                                <li>Use a strong and unique password</li>
                                                <li>Never share your login credentials</li>
                                                <li>Change your password regularly</li>
                                            </ul>
                                        </td>
                                    </tr>
                                </table>

                                <!-- CTA -->
                                <div style="text-align:center; margin:35px 0;">
                                    <a href="https://begin2code.onrender.com/index"
                                       style="background:#ef4444; color:#ffffff;
                                       text-decoration:none; padding:14px 34px;
                                       border-radius:30px; font-size:15px;
                                       display:inline-block; font-weight:600;">
                                        Login to Account →
                                    </a>
                                </div>

                                <p style="font-size:14px; color:#6c757d;">
                                    If you need help, feel free to reply to this email.
                                </p>

                                <p style="margin-bottom:0;">
                                    Stay safe,<br>
                                    <strong>Team Begin2Code</strong>
                                </p>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td style="background:#f1f3f5; padding:18px; text-align:center;
                                font-size:12px; color:#6c757d;">
                                © 2026 Begin2Code · All rights reserved
                            </td>
                        </tr>

                    </table>

                </td>
            </tr>
        </table>
    </body>
    </html>
    """

    mail.send(msg)


    