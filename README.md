
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Muhammed Akif Sayin | Offensive Security Specialist | Cybersecurity & Pentesting Portfolio">
    <title>DedCrowd | Muhammed Akif Sayin</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #0d1117;
            color: #c9d1d9;
            overflow-x: hidden;
        }
        header {
            background-color: rgba(22, 27, 34, 0.95);
            padding: 60px 20px;
            text-align: center;
            background-image: url('https://source.unsplash.com/1600x900/?cybersecurity,hacker');
            background-size: cover;
            background-blend-mode: overlay;
            position: relative;
        }
        header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 1;
        }
        .container {
            width: 90%;
            max-width: 1100px;
            margin: 40px auto;
            padding: 40px;
            background-color: rgba(22, 27, 34, 0.95);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
            border-radius: 8px;
            position: relative;
            z-index: 2;
        }
        h1, h2, h3 {
            color: #00ff7f;
        }
        a {
            color: #00ff7f;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        footer {
            text-align: center;
            padding: 20px;
            background-color: rgba(22, 27, 34, 0.95);
            color: #c9d1d9;
        }
        .contact-info {
            margin: 10px 0;
        }
        @keyframes cyber-glow {
            0% { text-shadow: 0 0 5px #00ff7f; }
            50% { text-shadow: 0 0 20px #00ff7f; }
            100% { text-shadow: 0 0 5px #00ff7f; }
        }
        .glow-text {
            animation: cyber-glow 1.5s infinite;
            font-size: 2.5rem;
        }
        .animated-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: url('https://source.unsplash.com/1600x900/?technology,hacker') no-repeat center center/cover;
            filter: blur(5px);
            opacity: 0.3;
        }
    </style>
</head>
<body>
    <div class="animated-bg"></div>
    <header>
        <div class="container">
            <h1 class="glow-text">Muhammed Akif SAYIN | ~ DedCrowd ~</h1>
            <p class="glow-text">🔒 Offensive Hacker | Web & Mobile Pentester | Cybersecurity Specialist</p>
        </div>
    </header>

    <section id="about">
        <div class="container">
            <h2>About Me</h2>
            <p>Hi, I'm <strong>Muhammed Akif Sayin</strong>, a passionate <strong>Offensive Security Specialist</strong> with hands-on experience in web and mobile pentesting. I thrive in learning advanced security techniques and developing cybersecurity solutions. Currently, I am working at Ege Yurt Grup and Kamyoon, focusing on enhancing web and network security.</p>
        </div>
    </section>

    <section id="certifications">
        <div class="container">
            <h2>Certifications</h2>
            <ul>
                <li><strong>AWS Certified Cloud Practitioner (CLF-C02)</strong> - Cloud Concepts (Dec 2024)</li>
                <li><strong>CompTIA PenTest+ (PT0-002)</strong> - Penetration Testing (Dec 2024)</li>
                <li><strong>CompTIA Security+ (SY0-701)</strong> - Security Monitoring & Threat Management (Dec 2024)</li>
                <li><strong>ISC2 CISSP (2024)</strong> - Information Security, Security Operations (Dec 2024)</li>
                <li><strong>Ubuntu Linux: Network Administration</strong> (Dec 2024)</li>
                <li><strong>Advanced Cyber Security Expertise (260 Hours)</strong> - Bilisim Academy (Oct 2024)</li>
                <li><strong>FSMSEM Cybersecurity Certification (120 Hours)</strong> - Network Security, Risk Management (Sep 2024)</li>
                <li><strong>Cisco - CCNAv7: Introduction to Networks</strong> (May 2024)</li>
            </ul>
        </div>
    </section>

    <section id="contact">
        <div class="container">
            <h2>Contact Me</h2>
            <p class="contact-info">Email: <a href="mailto:akif@hackermail.com">akif@hackermail.com</a></p>
            <p class="contact-info">Secondary Email: <a href="mailto:dedcrowd@hackermail.com">dedcrowd@hackermail.com</a></p>
            <p class="contact-info">GitHub: <a href="https://github.com/hunthack3r" target="_blank">github.com/hunthack3r</a></p>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2024 Muhammed Akif Sayin | DedCrowd.io</p>
        </div>
    </footer>
</body>
</html>
