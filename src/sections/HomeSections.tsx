import { Action } from '../components/Action';
import { activities, audiences, questions } from '../data/home';
import stillLife from '../assets/images/still-life.webp';
import styles from './HomeSections.module.scss';

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
  return (
    <section
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
        <div className={styles.activityList}>
          {activities.map(({ number, title, copy }) => (
            <article className={styles.activity} key={number}>
              <span className={styles.activityNumber}>{number}</span>
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
  return (
    <section
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
          <span>Портрет руководителя — после согласования</span>
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
