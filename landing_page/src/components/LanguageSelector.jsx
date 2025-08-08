import React from 'react';

export default function LanguageSelector({ onLanguageChange, currentLang }) {
  return (
    <select
      className="form-control"
      style={{ width: '130px' }}
      value={currentLang}
      onChange={(e) => onLanguageChange(e.target.value)}
    >
      <option value="en">English</option>
      <option value="es">Español</option>
    </select>
  );
}
