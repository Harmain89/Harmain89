import base64
import os

png_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'series-ai-lead-flow.png')
svg_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'series-ai-lead-flow.svg')

with open(png_path, 'rb') as f:
    b64_data = base64.b64encode(f.read()).decode('ascii')

svg_content = f'''<svg width="100%" height="100%" viewBox="0 0 2011 782" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<defs>
  <!-- Glow filters -->
  <filter id="glowGreen" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="3" result="blur" />
    <feMerge>
      <feMergeNode in="blur" />
      <feMergeNode in="SourceGraphic" />
    </feMerge>
  </filter>
  <filter id="glowGreenStrong" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="5" result="blur1" />
    <feGaussianBlur stdDeviation="2.5" result="blur2" />
    <feMerge>
      <feMergeNode in="blur1" />
      <feMergeNode in="blur2" />
      <feMergeNode in="SourceGraphic" />
    </feMerge>
  </filter>
  <filter id="glowBlue" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="3.5" result="blur" />
    <feMerge>
      <feMergeNode in="blur" />
      <feMergeNode in="SourceGraphic" />
    </feMerge>
  </filter>
  <filter id="glowPurple" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="3.5" result="blur" />
    <feMerge>
      <feMergeNode in="blur" />
      <feMergeNode in="SourceGraphic" />
    </feMerge>
  </filter>
  <filter id="glowAmber" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="3" result="blur" />
    <feMerge>
      <feMergeNode in="blur" />
      <feMergeNode in="SourceGraphic" />
    </feMerge>
  </filter>

  <!-- Gradients -->
  <linearGradient id="scanGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#00e599" stop-opacity="0" />
    <stop offset="25%" stop-color="#58a6ff" stop-opacity="0.35" />
    <stop offset="50%" stop-color="#00e599" stop-opacity="0.75" />
    <stop offset="75%" stop-color="#58a6ff" stop-opacity="0.35" />
    <stop offset="100%" stop-color="#00e599" stop-opacity="0" />
  </linearGradient>
</defs>

<style type="text/css">
  @keyframes flowDash {{
    from {{ stroke-dashoffset: 28; }}
    to {{ stroke-dashoffset: 0; }}
  }}
  @keyframes pulseNodeGlow {{
    0%, 100% {{
      r: 4;
      fill: #00e599;
      filter: drop-shadow(0 0 3px #00e599);
    }}
    50% {{
      r: 6.5;
      fill: #58a6ff;
      filter: drop-shadow(0 0 7px #58a6ff);
    }}
  }}
  @keyframes pulseOrangeGlow {{
    0%, 100% {{
      r: 4;
      fill: #ff6d5a;
      filter: drop-shadow(0 0 3px #ff6d5a);
    }}
    50% {{
      r: 6;
      fill: #d29922;
      filter: drop-shadow(0 0 7px #d29922);
    }}
  }}
  @keyframes openAiPulse {{
    0%, 100% {{
      stroke: #00e599;
      stroke-opacity: 0.35;
      stroke-width: 1.5;
    }}
    50% {{
      stroke: #58a6ff;
      stroke-opacity: 0.9;
      stroke-width: 2.8;
    }}
  }}

  .flow-green {{
    stroke-dasharray: 8 6 !important;
    animation: flowDash 1.2s linear infinite;
    stroke: #00e599 !important;
    stroke-width: 2.2 !important;
    filter: url(#glowGreen);
  }}
  .flow-blue {{
    stroke-dasharray: 8 6 !important;
    animation: flowDash 1.3s linear infinite;
    stroke: #58a6ff !important;
    stroke-width: 2.2 !important;
    filter: url(#glowBlue);
  }}
  .flow-purple {{
    stroke-dasharray: 8 6 !important;
    animation: flowDash 1.3s linear infinite;
    stroke: #9d72ff !important;
    stroke-width: 2.2 !important;
    filter: url(#glowPurple);
  }}
  .flow-amber {{
    stroke-dasharray: 7 5 !important;
    animation: flowDash 1.4s linear infinite;
    stroke: #e3b341 !important;
    stroke-width: 2.0 !important;
    filter: url(#glowAmber);
  }}
  .flow-coral {{
    stroke-dasharray: 6 5 !important;
    animation: flowDash 1.8s linear infinite;
    stroke: #ff7b72 !important;
    stroke-width: 1.8 !important;
  }}
  .pulse-circle {{
    animation: pulseNodeGlow 2.2s ease-in-out infinite;
  }}
  .pulse-orange {{
    animation: pulseOrangeGlow 2.5s ease-in-out infinite;
  }}
  .ai-border-glow {{
    animation: openAiPulse 2.8s ease-in-out infinite;
  }}
</style>

<!-- Base Canvas Image -->
<image href="data:image/png;base64,{b64_data}" width="2011" height="782" preserveAspectRatio="xMidYMid meet" />

<!-- Flowing Connection Lines -->
<g id="animated-flow-wires" pointer-events="none" fill="none">
  <!-- Node 1 -> Node 2 -->
  <path d="M 178 437 L 268 437" class="flow-green" />
  <!-- Node 2 -> Node 3 -->
  <path d="M 333 437 L 414 437" class="flow-green" />
  <!-- Node 3 -> Node 4 (true) -->
  <path d="M 476 428 C 515 428, 525 437, 565 437" class="flow-green" />
  <!-- Node 3 -> Respond 400 (false) -->
  <path d="M 476 447 C 505 447, 505 460, 505 480 L 505 515 C 505 525, 495 525, 480 525 L 400 525 C 388 525, 388 535, 388 550 L 388 565 C 388 576, 400 576, 416 576" class="flow-coral" />
  <!-- Node 4 -> Node 5 (OpenAI) -->
  <path d="M 630 437 L 710 437" class="flow-blue" />
  <!-- Node 5 -> Node 6 -->
  <path d="M 854 437 L 904 437" class="flow-green" />
  <!-- Node 6 -> Node 7 (Human Escalation?) -->
  <path d="M 969 437 L 1050 437" class="flow-green" />
  
  <!-- Tier 1: Escalation Branch -->
  <path d="M 1112 426 C 1154 426, 1154 291, 1196 291" class="flow-purple" />
  <path d="M 1260 291 L 1350 291" class="flow-purple" />
  <path d="M 1416 291 L 1495 291" class="flow-purple" />
  <path d="M 1561 291 C 1610 291, 1610 437, 1649 437" class="flow-purple" />

  <!-- Tier 2: Hot Lead Branch -->
  <path d="M 1112 448 C 1155 448, 1155 495, 1198 495" class="flow-green" />
  <path d="M 1262 485 C 1307 485, 1307 437, 1352 437" class="flow-green" />
  <path d="M 1416 437 C 1456 437, 1456 377, 1496 377" class="flow-blue" />
  <path d="M 1559 377 C 1604 377, 1604 437, 1649 437" class="flow-green" />

  <!-- Tier 3: Warm Lead Branch -->
  <path d="M 1262 505 C 1306 505, 1306 571, 1351 571" class="flow-amber" />
  <path d="M 1417 560 C 1457 560, 1457 514, 1497 514" class="flow-green" />
  <path d="M 1560 514 C 1605 514, 1605 437, 1649 437" class="flow-green" />

  <!-- Tier 4: Nurture Lead Branch -->
  <path d="M 1417 582 C 1457 582, 1457 632, 1498 632" class="flow-amber" />
  <path d="M 1561 632 C 1605 632, 1605 437, 1649 437" class="flow-amber" />

  <!-- Final Delivery: Format -> 200 Success -->
  <path d="M 1714 437 L 1795 437" class="flow-green" />
</g>

<!-- Pulsing Connection Ports -->
<g id="pulsing-connection-ports" pointer-events="none">
  <!-- Node ports -->
  <circle cx="178" cy="437" r="4" class="pulse-circle" />
  <circle cx="268" cy="437" r="4" class="pulse-circle" />
  <circle cx="333" cy="437" r="4" class="pulse-circle" />
  <circle cx="414" cy="437" r="4" class="pulse-circle" />
  <circle cx="476" cy="428" r="4" class="pulse-circle" />
  <circle cx="476" cy="447" r="3.5" class="pulse-orange" />
  <circle cx="416" cy="576" r="3.5" class="pulse-orange" />
  <circle cx="565" cy="437" r="4" class="pulse-circle" />
  <circle cx="630" cy="437" r="4" class="pulse-circle" />
  <circle cx="710" cy="437" r="4" class="pulse-circle" />
  <circle cx="854" cy="437" r="4" class="pulse-circle" />
  <circle cx="904" cy="437" r="4" class="pulse-circle" />
  <circle cx="969" cy="437" r="4" class="pulse-circle" />
  <circle cx="1050" cy="437" r="4" class="pulse-circle" />
  <circle cx="1112" cy="426" r="4" class="pulse-circle" />
  <circle cx="1112" cy="448" r="4" class="pulse-circle" />
  
  <circle cx="1196" cy="291" r="4" class="pulse-circle" />
  <circle cx="1260" cy="291" r="4" class="pulse-circle" />
  <circle cx="1350" cy="291" r="4" class="pulse-circle" />
  <circle cx="1416" cy="291" r="4" class="pulse-circle" />
  <circle cx="1495" cy="291" r="4" class="pulse-circle" />
  <circle cx="1561" cy="291" r="4" class="pulse-circle" />

  <circle cx="1198" cy="495" r="4" class="pulse-circle" />
  <circle cx="1262" cy="485" r="4" class="pulse-circle" />
  <circle cx="1262" cy="505" r="3.5" class="pulse-orange" />
  <circle cx="1352" cy="437" r="4" class="pulse-circle" />
  <circle cx="1416" cy="437" r="4" class="pulse-circle" />
  <circle cx="1496" cy="377" r="4" class="pulse-circle" />
  <circle cx="1559" cy="377" r="4" class="pulse-circle" />

  <circle cx="1351" cy="571" r="3.5" class="pulse-orange" />
  <circle cx="1417" cy="560" r="4" class="pulse-circle" />
  <circle cx="1417" cy="582" r="3.5" class="pulse-orange" />
  <circle cx="1497" cy="514" r="4" class="pulse-circle" />
  <circle cx="1560" cy="514" r="4" class="pulse-circle" />
  <circle cx="1498" cy="632" r="3.5" class="pulse-orange" />
  <circle cx="1561" cy="632" r="3.5" class="pulse-orange" />

  <circle cx="1649" cy="437" r="4.5" class="pulse-circle" />
  <circle cx="1714" cy="437" r="4.5" class="pulse-circle" />
  <circle cx="1795" cy="437" r="4.5" class="pulse-circle" />
  <circle cx="1859" cy="437" r="5" class="pulse-circle" />
</g>

<!-- Highlight Aura around OpenAI Node -->
<rect x="710" y="406" width="144" height="63" rx="8" fill="none" class="ai-border-glow" pointer-events="none" />

<!-- Dynamic Traveling Data Packets -->
<g id="traveling-data-packets" pointer-events="none">
  <!-- Node 1 -> Node 2 -->
  <circle r="4" fill="#00e599" filter="url(#glowGreenStrong)">
    <animateMotion path="M 178 437 L 268 437" dur="0.9s" repeatCount="indefinite" />
  </circle>
  <circle r="3" fill="#58a6ff" filter="url(#glowBlue)">
    <animateMotion path="M 178 437 L 268 437" dur="0.9s" begin="0.45s" repeatCount="indefinite" />
  </circle>

  <!-- Node 2 -> Node 3 -->
  <circle r="4" fill="#00e599" filter="url(#glowGreenStrong)">
    <animateMotion path="M 333 437 L 414 437" dur="0.8s" repeatCount="indefinite" />
  </circle>

  <!-- Node 3 -> Node 4 (true) -->
  <circle r="4" fill="#00e599" filter="url(#glowGreenStrong)">
    <animateMotion path="M 476 428 C 515 428, 525 437, 565 437" dur="0.9s" repeatCount="indefinite" />
  </circle>

  <!-- Node 3 -> Respond 400 (false branch - rejection) -->
  <circle r="3.5" fill="#ff7b72">
    <animateMotion path="M 476 447 C 505 447, 505 460, 505 480 L 505 515 C 505 525, 495 525, 480 525 L 400 525 C 388 525, 388 535, 388 550 L 388 565 C 388 576, 400 576, 416 576" dur="2.6s" repeatCount="indefinite" />
  </circle>

  <!-- Node 4 -> OpenAI -->
  <circle r="4.5" fill="#58a6ff" filter="url(#glowBlue)">
    <animateMotion path="M 630 437 L 710 437" dur="0.8s" repeatCount="indefinite" />
  </circle>
  <circle r="3" fill="#00e599" filter="url(#glowGreenStrong)">
    <animateMotion path="M 630 437 L 710 437" dur="0.8s" begin="0.4s" repeatCount="indefinite" />
  </circle>

  <!-- OpenAI -> Parse -->
  <circle r="4" fill="#00e599" filter="url(#glowGreenStrong)">
    <animateMotion path="M 854 437 L 904 437" dur="0.6s" repeatCount="indefinite" />
  </circle>

  <!-- Parse -> Human Escalation? -->
  <circle r="4" fill="#00e599" filter="url(#glowGreenStrong)">
    <animateMotion path="M 969 437 L 1050 437" dur="0.8s" repeatCount="indefinite" />
  </circle>

  <!-- Tier 1: Escalation Branch -->
  <circle r="4" fill="#9d72ff" filter="url(#glowPurple)">
    <animateMotion path="M 1112 426 C 1154 426, 1154 291, 1196 291" dur="1.3s" repeatCount="indefinite" />
  </circle>
  <circle r="4" fill="#9d72ff" filter="url(#glowPurple)">
    <animateMotion path="M 1260 291 L 1350 291" dur="0.9s" repeatCount="indefinite" />
  </circle>
  <circle r="4" fill="#9d72ff" filter="url(#glowPurple)">
    <animateMotion path="M 1416 291 L 1495 291" dur="0.8s" repeatCount="indefinite" />
  </circle>
  <circle r="4" fill="#9d72ff" filter="url(#glowPurple)">
    <animateMotion path="M 1561 291 C 1610 291, 1610 437, 1649 437" dur="1.4s" repeatCount="indefinite" />
  </circle>

  <!-- Tier 2: Hot Lead Branch -->
  <circle r="4" fill="#00e599" filter="url(#glowGreenStrong)">
    <animateMotion path="M 1112 448 C 1155 448, 1155 495, 1198 495" dur="1.2s" repeatCount="indefinite" />
  </circle>
  <circle r="4" fill="#00e599" filter="url(#glowGreenStrong)">
    <animateMotion path="M 1262 485 C 1307 485, 1307 437, 1352 437" dur="1.1s" repeatCount="indefinite" />
  </circle>
  <circle r="4" fill="#58a6ff" filter="url(#glowBlue)">
    <animateMotion path="M 1416 437 C 1456 437, 1456 377, 1496 377" dur="1.0s" repeatCount="indefinite" />
  </circle>
  <circle r="4" fill="#00e599" filter="url(#glowGreenStrong)">
    <animateMotion path="M 1559 377 C 1604 377, 1604 437, 1649 437" dur="1.2s" repeatCount="indefinite" />
  </circle>

  <!-- Tier 3: Warm Lead Branch -->
  <circle r="3.8" fill="#e3b341" filter="url(#glowAmber)">
    <animateMotion path="M 1262 505 C 1306 505, 1306 571, 1351 571" dur="1.3s" repeatCount="indefinite" />
  </circle>
  <circle r="3.8" fill="#38ef7d" filter="url(#glowGreen)">
    <animateMotion path="M 1417 560 C 1457 560, 1457 514, 1497 514" dur="1.0s" repeatCount="indefinite" />
  </circle>
  <circle r="3.8" fill="#38ef7d" filter="url(#glowGreen)">
    <animateMotion path="M 1560 514 C 1605 514, 1605 437, 1649 437" dur="1.2s" repeatCount="indefinite" />
  </circle>

  <!-- Tier 4: Nurture Lead Branch -->
  <circle r="3.5" fill="#e3b341" filter="url(#glowAmber)">
    <animateMotion path="M 1417 582 C 1457 582, 1457 632, 1498 632" dur="1.1s" repeatCount="indefinite" />
  </circle>
  <circle r="3.5" fill="#e3b341" filter="url(#glowAmber)">
    <animateMotion path="M 1561 632 C 1605 632, 1605 437, 1649 437" dur="1.2s" repeatCount="indefinite" />
  </circle>

  <!-- Final Delivery -> 200 Success -->
  <circle r="4.5" fill="#00e599" filter="url(#glowGreenStrong)">
    <animateMotion path="M 1714 437 L 1795 437" dur="0.8s" repeatCount="indefinite" />
  </circle>
  <circle r="3" fill="#58a6ff" filter="url(#glowBlue)">
    <animateMotion path="M 1714 437 L 1795 437" dur="0.8s" begin="0.4s" repeatCount="indefinite" />
  </circle>
</g>

<!-- Subtle Ambient Scanning Light Beam -->
<g opacity="0.28" pointer-events="none">
  <line x1="60" y1="0" x2="1950" y2="0" stroke="url(#scanGrad)" stroke-width="2.5">
    <animateTransform attributeName="transform" type="translate" from="0 40" to="0 740" dur="5.5s" repeatCount="indefinite" />
  </line>
</g>
</svg>'''

with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(svg_content)

print(f'Successfully generated {svg_path}, size: {len(svg_content)} bytes')
