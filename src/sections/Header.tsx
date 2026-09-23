import { useEffect, useRef, useState } from 'react';

import { Action } from '../components/Action';
import styles from './Header.module.scss';

const links = [
  { label: 'О нас', href: '#mission' },
  { label: 'Кому помогаем', href: '#audience' },
  { label: 'Второй сезон', href: '#season' },
];

export function Header() {
  const [menuOpen, setMenuOpen] = useState(false);
  const menuButton = useRef<HTMLButtonElement>(null);
  const menuPanel = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!menuOpen) return;
    menuPanel.current?.querySelector('a')?.focus();
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        setMenuOpen(false);
        menuButton.current?.focus();
      } else if (event.key === 'Tab') {
        const items = [
          menuButton.current,
          ...Array.from(menuPanel.current?.querySelectorAll('a') ?? []),
        ].filter(
          (item): item is HTMLButtonElement | HTMLAnchorElement =>
            item !== null,
        );
        const first = items[0];
        const last = items.at(-1);
        if (event.shiftKey && document.activeElement === first && last) {
          event.preventDefault();
          last.focus();
        } else if (
          !event.shiftKey &&
          document.activeElement === last &&
          first
        ) {
          event.preventDefault();
          first.focus();
        }
      }
    };
    document.addEventListener('keydown', onKeyDown);
    return () => document.removeEventListener('keydown', onKeyDown);
  }, [menuOpen]);

  const closeMenu = () => setMenuOpen(false);

  return (
    <header className={styles.header}>
      <div className={`container ${styles.inner}`}>
        <a
          className={styles.brand}
          href="#top"
          aria-label="ДРУЖИМ — наверх"
          onClick={closeMenu}
        >
          ДРУЖИМ
        </a>
        <nav className={styles.desktopNav} aria-label="Основная навигация">
          {links.map(({ label, href }) => (
            <a key={href} href={href}>
              {label}
            </a>
          ))}
        </nav>
        <Action className={styles.desktopAction} href="#contact">
          Связаться
        </Action>
        <button
          ref={menuButton}
          className={styles.menuButton}
          type="button"
          aria-expanded={menuOpen}
          aria-controls="mobile-navigation"
          onClick={() => setMenuOpen((open) => !open)}
        >
          {menuOpen ? 'Закрыть' : 'Меню'}
        </button>
      </div>
      {menuOpen && (
        <div
          id="mobile-navigation"
          ref={menuPanel}
          className={styles.mobilePanel}
        >
          <nav aria-label="Мобильная навигация">
            {[...links, { label: 'Контакты', href: '#contact' }].map(
              ({ label, href }) => (
                <a key={href} href={href} onClick={closeMenu}>
                  {label}
                </a>
              ),
            )}
          </nav>
          <Action href="#season" className={styles.mobileAction}>
            Узнать о группах
          </Action>
        </div>
      )}
    </header>
  );
}
