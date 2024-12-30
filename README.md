
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DedCrowd | Muhammed Akif Sayin</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            font-family: 'Orbitron', sans-serif;
            background-color: black;
            color: #33ff33;
            overflow: hidden;
        }
        .container {
            text-align: center;
            margin-top: 20vh;
        }
        h1 {
            font-size: 4em;
            margin: 0;
            text-shadow: 0 0 10px #33ff33;
            animation: glitch 1.5s infinite alternate;
        }
        p {
            font-size: 1.2em;
            margin: 20px 0;
            text-shadow: 0 0 5px #33ff33;
        }
        .hidden-message {
            font-size: 1.5em;
            opacity: 0;
            animation: reveal 4s forwards 2s;
        }
        @keyframes glitch {
            0% { transform: skew(0deg); }
            20% { transform: skew(-5deg); }
            40% { transform: skew(5deg); }
            60% { transform: skew(-5deg); }
            80% { transform: skew(5deg); }
            100% { transform: skew(0deg); }
        }
        @keyframes reveal {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .terminal {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 40vh;
            background: rgba(0, 0, 0, 0.8);
            color: #33ff33;
            font-family: monospace;
            padding: 20px;
            box-shadow: 0 0 20px #33ff33;
            overflow: hidden;
        }
        .code {
            white-space: pre-line;
            line-height: 1.5em;
            animation: type 5s steps(40) 1s forwards;
        }
        @keyframes type {
            from { width: 0; }
            to { width: 100%; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>You Have Been Hacked</h1>
        <p class="hidden-message">Don't let this happen to you. Stay secure.</p>
    </div>
    
    <div class="terminal">
        <div class="code">
            root@kali:~# ls /home/dedcrowd
            Certifications.txt
            Projects
            Exploits
            
            root@kali:~# cat Certifications.txt
            - AWS Certified Cloud Practitioner (Dec 2024)
            - CompTIA PenTest+ (Dec 2024)
            - ISC2 CISSP (Dec 2024)
            - Ubuntu Linux Network Administration (Dec 2024)
            - Advanced Cybersecurity Expertise (Oct 2024)
            - Cisco CCNA v7 (May 2024)

            root@kali:~# _
        </div>
    </div>
</body>
</html>
