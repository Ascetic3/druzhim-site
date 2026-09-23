import { useEffect, useRef } from 'react';
import gsap from 'gsap';

import { Action } from '../components/Action';
import styles from './Hero.module.scss';

function DesktopPaths() {
  return (
    <svg
      className={styles.desktopPaths}
      data-motion="hero"
      viewBox="0 0 1440 648"
      preserveAspectRatio="none"
      aria-hidden="true"
    >
      <path d="M0 274 C260 280 350 362 720 362 C1050 362 1150 292 1440 274" />
      <path d="M1240 416 C1040 416 998 362 720 362" />
      <circle cx="720" cy="362" r="5" />
    </svg>
  );
}

function MobilePath() {
  return (
    <svg
      className={styles.mobilePath}
      viewBox="0 0 390 616"
      preserveAspectRatio="none"
      aria-hidden="true"
    >
      <path d="M0 316 C130 280 166 354 262 336 C308 326 348 330 390 308" />
      <circle cx="262" cy="336" r="4" />
    </svg>
  );
}

export function Hero() {
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    if (
      !window.matchMedia(
        '(min-width: 900px) and (prefers-reduced-motion: no-preference)',
      ).matches
    )
      return;
    const section = sectionRef.current;
    if (!section) return;
    const paths = section.querySelectorAll<SVGPathElement>(
      'svg[data-motion="hero"] path',
    );
    const node = section.querySelector<SVGCircleElement>(
      'svg[data-motion="hero"] circle',
    );
    const context = gsap.context(() => {
      paths.forEach((path, index) => {
        const length = path.getTotalLength();
        gsap.set(path, { strokeDasharray: length, strokeDashoffset: length });
        gsap.to(path, {
          strokeDashoffset: 0,
          duration: 0.72,
          delay: index === 0 ? 0.18 : 0.38,
          ease: 'power2.out',
        });
      });
      if (node)
        gsap.fromTo(
          node,
          { opacity: 0 },
          { opacity: 1, duration: 0.4, delay: 0.65 },
        );
    }, section);
    return () => context.revert();
  }, []);

  return (
    <section
      ref={sectionRef}
      id="top"
      className={styles.hero}
      aria-labelledby="hero-title"
    >
      <div className={styles.inner}>
        <h1 id="hero-title" className={styles.heading}>
          <span>У каждого — свой путь.</span> <span>Рядом — ДРУЖИМ.</span>
        </h1>
        <DesktopPaths />
        <MobilePath />
        <p className={styles.copy}>
          Помогаем детям, молодежи и семьям развивать навыки, находить поддержку
          и становиться самостоятельнее.
        </p>
        <Action href="#season" className={styles.action}>
          Узнать о группах
        </Action>
      </div>
    </section>
  );
}
