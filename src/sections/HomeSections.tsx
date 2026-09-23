import { useEffect, useRef } from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

import { Action } from '../components/Action';
import { activities, audiences, questions } from '../data/home';
import stillLife from '../assets/images/still-life.webp';
import styles from './HomeSections.module.scss';

gsap.registerPlugin(ScrollTrigger);

export function Audience() {
  return (
    <section
      id="audience"
      className={styles.audience}
      aria-labelledby="audience-title"
    >
      <div className={`container ${styles.sectionInner}`}>
        <h2 id="audience-title" className={styles.audienceHeading}>
          Кому мы
          <br className={styles.mobileOnly} /> помогаем
        </h2>
        <p className={styles.audienceIntro}>
          Психологическая и социальная поддержка. Развитие практических и
          социальных навыков.
        </p>
        <div className={styles.audienceList}>
          {audiences.map(({ title, copy }) => (
            <div className={styles.audienceRow} key={title}>
              <span className={styles.audienceNode} aria-hidden="true" />
              <h3>{title}</h3>
              <p>{copy}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export function FosterFamilies() {
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    const media = gsap.matchMedia();
    media.add(
      '(min-width: 900px) and (prefers-reduced-motion: no-preference)',
      () => {
        const section = sectionRef.current;
        const image = section?.querySelector('img');
        if (!section || !image) return;
        gsap.fromTo(
          image,
          { clipPath: 'inset(0 100% 0 0)' },
          {
            clipPath: 'inset(0 0% 0 0)',
            duration: 0.4,
            ease: 'power2.out',
            scrollTrigger: { trigger: section, start: 'top 80%', once: true },
          },
        );
      },
    );
    return () => media.revert();
  }, []);

  return (
    <section
      ref={sectionRef}
      id="families"
      className={styles.foster}
      aria-labelledby="foster-title"
    >
      <div className={`container ${styles.sectionInner}`}>
        <p className={styles.fosterLabel}>Замещающие семьи</p>
        <h2 id="foster-title" className={styles.fosterHeading}>
          Семье тоже
          <br className={styles.mobileOnly} /> нужна поддержка
        </h2>
        <figure className={styles.fosterFigure}>
          <img
            src={stillLife}
            alt="Светлая комната для встреч; иллюстративный визуальный референс"
            loading="lazy"
          />
          <figcaption>
            Визуальный референс.
            <br className={styles.mobileOnly} /> Фотографию центра согласуем.
          </figcaption>
        </figure>
        <p className={styles.fosterLead}>
          Особое внимание — семьям, связанным с опекой, приемным родительством и
          усыновлением.
        </p>
        <p className={styles.fosterCopy}>
          Поддержка важна и детям в учреждениях, и выпускникам, которые начинают
          самостоятельную жизнь.
        </p>
        <a className={styles.textLink} href="#contact">
          Обсудить свою ситуацию
        </a>
        <svg
          className={styles.fosterLines}
          viewBox="0 0 1440 840"
          preserveAspectRatio="none"
          aria-hidden="true"
        >
          <path d="M760 790 C940 722 1170 788 1440 700 M1110 774 C1210 774 1290 814 1440 824" />
          <circle cx="1110" cy="774" r="4" />
        </svg>
      </div>
    </section>
  );
}

export function Activities() {
  return (
    <section
      id="activities"
      className={styles.activities}
      aria-labelledby="activities-title"
    >
      <div className={`container ${styles.sectionInner}`}>
        <h2 id="activities-title" className={styles.activitiesHeading}>
          Что происходит
          <br />в «ДРУЖИМ»
        </h2>
        <svg
          className={styles.activityLines}
          viewBox="0 0 1440 692"
          preserveAspectRatio="none"
          aria-hidden="true"
        >
          <path d="M88 406 C240 390 390 460 536 462 C720 462 778 382 984 382 C1130 382 1250 404 1360 386" />
        </svg>
        <div className={styles.activityList}>
          {activities.map(({ number, title, copy }) => (
            <article className={styles.activity} key={number}>
              <span className={styles.activityNumber}>{number}</span>
              <span className={styles.activityNode} aria-hidden="true" />
              <h3>{title}</h3>
              <p>{copy}</p>
            </article>
          ))}
        </div>
        <p className={styles.activitiesNote}>
          Конкретные занятия и состав групп уточняются.
        </p>
      </div>
    </section>
  );
}

export function Season() {
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    const media = gsap.matchMedia();
    media.add(
      '(min-width: 900px) and (prefers-reduced-motion: no-preference)',
      () => {
        const section = sectionRef.current;
        if (!section) return;
        section
          .querySelectorAll<SVGPathElement>('svg[data-motion="season"] path')
          .forEach((path) => {
            const length = path.getTotalLength();
            gsap.fromTo(
              path,
              { strokeDasharray: length, strokeDashoffset: length },
              {
                strokeDashoffset: 0,
                duration: 0.5,
                ease: 'power2.out',
                scrollTrigger: {
                  trigger: section,
                  start: 'top 75%',
                  once: true,
                },
              },
            );
          });
      },
    );
    return () => media.revert();
  }, []);

  return (
    <section
      ref={sectionRef}
      id="season"
      className={styles.season}
      aria-labelledby="season-title"
    >
      <div className={`container ${styles.sectionInner}`}>
        <h2 id="season-title">
          Второй сезон.
          <br />
          Новые встречи.
        </h2>
        <p className={styles.seasonLead}>
          Открывается запись в группы второго сезона.
        </p>
        <p className={styles.seasonNote}>
          Возраст, расписание и условия участия уточняются.
        </p>
        <svg
          className={styles.seasonLines}
          data-motion="season"
          viewBox="0 0 1440 544"
          preserveAspectRatio="none"
          aria-hidden="true"
        >
          <path d="M760 0 C820 40 790 310 930 324 M760 544 C830 470 822 340 930 324 M1110 544 C1030 472 1030 360 930 324 M930 324 H1080" />
          <circle cx="930" cy="324" r="5" />
        </svg>
        <svg
          className={styles.seasonMobileLines}
          viewBox="0 0 390 676"
          preserveAspectRatio="none"
          aria-hidden="true"
        >
          <path d="M0 450 C124 450 130 492 195 492 M390 450 C260 450 260 492 195 492 M195 492 V528" />
          <circle cx="195" cy="492" r="4" />
        </svg>
        <Action inverse href="#contact" className={styles.seasonAction}>
          Узнать о группах
        </Action>
      </div>
    </section>
  );
}

export function Mission() {
  return (
    <section
      id="mission"
      className={styles.mission}
      aria-labelledby="mission-title"
    >
      <div className={`container ${styles.sectionInner}`}>
        <p className={styles.missionLabel}>Наша миссия</p>
        <h2 id="mission-title">
          Больше самостоятельности.
          <br />
          Больше возможностей
          <br />
          быть собой.
        </h2>
        <p className={styles.missionCopy}>
          Создаем безопасное и поддерживающее пространство, где дети, молодежь и
          семьи могут раскрывать потенциал и уверенно строить будущее без
          барьеров и стереотипов.
        </p>
        <svg
          className={styles.missionLines}
          viewBox="0 0 1440 676"
          preserveAspectRatio="none"
          aria-hidden="true"
        >
          <path d="M0 434 C220 430 248 532 588 532 M0 630 C240 630 250 532 588 532" />
          <circle cx="588" cy="532" r="4" />
        </svg>
      </div>
    </section>
  );
}

export function Director() {
  return (
    <section
      id="director"
      className={styles.director}
      aria-labelledby="director-title"
    >
      <div className={`container ${styles.sectionInner}`}>
        <div className={styles.portrait}>
          Портрет руководителя
          <br />
          после согласования
        </div>
        <p className={styles.directorLabel}>Руководитель</p>
        <h2 id="director-title">
          Ирина Анатольевна
          <br />
          Малышева
        </h2>
        <p className={styles.directorLead}>
          Руководит организацией с 2025 года.
        </p>
        <p className={styles.directorCopy}>
          Объединяет опыт родителей и специалистов.
        </p>
        <p className={styles.directorNote}>
          Личную историю публикуем только после согласования.
        </p>
        <svg
          className={styles.directorLines}
          viewBox="0 0 1440 720"
          preserveAspectRatio="none"
          aria-hidden="true"
        >
          <path d="M1170 630 C1290 620 1280 512 1440 492" />
        </svg>
      </div>
    </section>
  );
}

export function Results() {
  return (
    <section
      id="results"
      className={styles.results}
      aria-labelledby="results-title"
    >
      <div className={`container ${styles.sectionInner}`}>
        <h2 id="results-title">Факты о «ДРУЖИМ»</h2>
        <div className={styles.facts}>
          <div>
            <strong>2025</strong>
            <p>Ирина Анатольевна приняла руководство организацией.</p>
          </div>
          <div>
            <strong>Второй сезон</strong>
            <p>Открывается запись в группы.</p>
          </div>
        </div>
        <p className={styles.resultsNote}>
          Результаты работы добавим после проверки данных.
        </p>
      </div>
    </section>
  );
}

export function Faq() {
  return (
    <section id="faq" className={styles.faq} aria-labelledby="faq-title">
      <div className={`container ${styles.sectionInner}`}>
        <h2 id="faq-title">
          Вопросы,
          <br className={styles.desktopOnly} /> с которых
          <br />
          можно начать
        </h2>
        <div className={styles.faqList}>
          {questions.map(({ question, answer }, index) => (
            <details key={question} open={index === 0 ? true : undefined}>
              <summary>
                {question}
                <span className={styles.faqIcon} aria-hidden="true" />
              </summary>
              <p>
                {answer ??
                  'Ответы об участии и контактах требуют согласования.'}
              </p>
            </details>
          ))}
          <p className={styles.faqNote}>
            Ответы об участии и контактах требуют согласования.
          </p>
        </div>
      </div>
    </section>
  );
}

export function Contact() {
  return (
    <section
      id="contact"
      className={styles.contact}
      aria-labelledby="contact-title"
    >
      <div className={`container ${styles.sectionInner}`}>
        <h2 id="contact-title">
          Начнем
          <br />с разговора
        </h2>
        <p>Расскажите, какая поддержка вам нужна.</p>
        <Action disabled className={styles.contactAction}>
          Связаться с «ДРУЖИМ»
        </Action>
        <p className={styles.contactNote}>TODO: подтвержденный канал связи</p>
        <svg
          className={styles.contactLines}
          viewBox="0 0 1440 500"
          preserveAspectRatio="none"
          aria-hidden="true"
        >
          <path d="M1440 0 C1240 200 1220 314 1010 342 M1440 160 C1270 290 1150 338 1010 342 M1440 480 C1260 372 1160 342 1010 342" />
          <circle cx="1010" cy="342" r="6" />
        </svg>
        <svg
          className={styles.contactMobileLines}
          viewBox="0 0 390 564"
          preserveAspectRatio="none"
          aria-hidden="true"
        >
          <path d="M390 296 C274 296 252 328 195 336 M0 296 C112 296 130 334 195 336" />
          <circle cx="195" cy="336" r="4" />
        </svg>
      </div>
    </section>
  );
}

export function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={`container ${styles.sectionInner}`}>
        <a className={styles.footerBrand} href="#top">
          ДРУЖИМ
        </a>
        <p className={styles.organization}>
          АНО «Центр социализации детей и молодежи „ДРУЖИМ“»
        </p>
        <nav aria-label="Навигация внизу страницы">
          <a href="#mission">О нас</a>
          <a className={styles.footerAudience} href="#audience">
            Кому помогаем
          </a>
          <a href="#season">Второй сезон</a>
        </nav>
        <p className={styles.footerNote}>
          <span className={styles.desktopOnly}>
            Контакты, реквизиты и правовые документы — после проверки.
          </span>
          <span className={styles.mobileOnly}>
            Контакты и правовые документы — после проверки.
          </span>
        </p>
      </div>
    </footer>
  );
}
