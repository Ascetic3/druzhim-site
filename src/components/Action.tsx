import type { ReactNode } from 'react';

import styles from './Action.module.scss';

type ActionProps = {
  children: ReactNode;
  href?: string;
  inverse?: boolean;
  disabled?: boolean;
  className?: string | undefined;
};

export function Action({
  children,
  href,
  inverse = false,
  disabled = false,
  className = '',
}: ActionProps) {
  const classes = [styles.action, inverse && styles.inverse, className]
    .filter(Boolean)
    .join(' ');
  if (disabled || !href) {
    return (
      <button className={classes} type="button" disabled>
        {children}
      </button>
    );
  }
  return (
    <a className={classes} href={href}>
      {children}
    </a>
  );
}
