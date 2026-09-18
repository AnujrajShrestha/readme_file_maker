export default function AnimatedBackground() {
  return (
    <div aria-hidden="true" className="pointer-events-none fixed inset-0 -z-10 overflow-hidden">
      <div className="grid-fade absolute inset-0 opacity-80" />
      <svg
        className="absolute left-1/2 top-0 h-[720px] w-[1200px] -translate-x-1/2 opacity-80"
        viewBox="0 0 1200 720"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <defs>
          <linearGradient id="g1" x1="0" y1="0" x2="1200" y2="720">
            <stop stopColor="#6366F1" stopOpacity=".42" />
            <stop offset=".5" stopColor="#22D3EE" stopOpacity=".08" />
            <stop offset="1" stopColor="#A855F7" stopOpacity=".35" />
          </linearGradient>
          <filter id="blur">
            <feGaussianBlur stdDeviation="28" />
          </filter>
        </defs>

        <ellipse className="float-slow" cx="240" cy="150" rx="220" ry="120" fill="#4F46E5" opacity=".12" filter="url(#blur)" />
        <ellipse className="float-slower" cx="960" cy="240" rx="230" ry="150" fill="#06B6D4" opacity=".09" filter="url(#blur)" />

        <path className="pulse-line" d="M0 450C170 350 220 570 390 450S640 330 790 450 1030 570 1200 410" stroke="url(#g1)" strokeWidth="1.5" />
        <path d="M0 500C180 400 260 620 430 490S650 370 820 500 1040 610 1200 470" stroke="url(#g1)" strokeOpacity=".28" />
        <path d="M80 90L1120 640M1120 90L80 640" stroke="#818CF8" strokeOpacity=".045" />

        {[...Array(18)].map((_, i) => (
          <circle
            key={i}
            cx={(i * 137) % 1120 + 40}
            cy={(i * 83) % 560 + 50}
            r={i % 3 === 0 ? 2 : 1}
            fill="#A5B4FC"
            opacity={i % 3 === 0 ? ".45" : ".2"}
          />
        ))}
      </svg>
    </div>
  );
}