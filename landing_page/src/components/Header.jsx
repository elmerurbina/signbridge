import React from 'react';
import LanguageSelector from './LanguageSelector';

export default function Header({ logoSrc, onLanguageChange, lang }) {
  return (
    <header className="header d-flex justify-content-between align-items-center px-4 py-3" style={{ backgroundColor: 'var(--deep-blue)', color: 'white' }}>
      <img src={logoSrc} alt="SignBridge Logo" style={{ height: '50px' }} />
      <LanguageSelector onLanguageChange={onLanguageChange} currentLang={lang} />
    </header>
  );
}
