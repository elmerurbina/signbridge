import React, { useState } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import LanguageSelector from './components/LanguageSelector';

const content = {
  en: {
    overview: `SignBridge is a platform connecting hearing and deaf communities through live sign language recognition and interpretation.`,
    functionalities: [
      "Real-time sign language recognition",
      "Speech to sign translation",
      "Multi-user video meetings",
      "Support for multiple languages"
    ],
    vision: "To break communication barriers and foster inclusion through technology.",
    mission: "Provide seamless communication tools for the deaf and hearing communities.",
    teamNote: "This project was presented on May 10 at the Mathematics Fair at National University of Engineering.",
    startMessage: "It will be available soon!"
  },
  es: {
    overview: `SignBridge es una plataforma que conecta a las comunidades sordas y oyentes mediante reconocimiento e interpretación en vivo de lenguaje de señas.`,
    functionalities: [
      "Reconocimiento en tiempo real de lenguaje de señas",
      "Traducción de voz a señas",
      "Reuniones por video con múltiples usuarios",
      "Soporte para múltiples idiomas"
    ],
    vision: "Romper barreras de comunicación y fomentar la inclusión a través de la tecnología.",
    mission: "Proveer herramientas de comunicación sin barreras para comunidades sordas y oyentes.",
    teamNote: "Este proyecto fue presentado el 10 de mayo en la Feria de Matemáticas en la Universidad Nacional de Ingeniería.",
    startMessage: "¡Estará disponible pronto!"
  }
};

export default function App() {
  const [lang, setLang] = useState('en');
  const [showStartMessage, setShowStartMessage] = useState(false);

  const t = content[lang];

  return (
    <div className="main-wrapper">
      <Header logoSrc="/assets/logo.png" onLanguageChange={setLang} lang={lang} />

      <main className="container">
        <section className="overview-box mb-4">
          <h2>{lang === 'en' ? 'Overview' : 'Resumen'}</h2>
          <p>{t.overview}</p>
        </section>

        <section className="mb-4">
          <h2>{lang === 'en' ? 'Functionalities' : 'Funcionalidades'}</h2>
          <ul>
            {t.functionalities.map((func, i) => (
              <li key={i}>{func}</li>
            ))}
          </ul>
        </section>

        <section className="mb-4">
          <h2>{lang === 'en' ? 'Vision' : 'Visión'}</h2>
          <p>{t.vision}</p>
        </section>

        <section className="mb-4">
          <h2>{lang === 'en' ? 'Mission' : 'Misión'}</h2>
          <p>{t.mission}</p>
        </section>

        <section className="mb-4">
          <h2>{lang === 'en' ? 'Team' : 'Equipo'}</h2>
          <div className="team-photos">
            <img src="/assets/team.jpg" alt="Team member 1" />

            {/* add more team photos as needed */}
          </div>
          <p className="team-note">{t.teamNote}</p>
        </section>

        <section className="mb-5">
          <h2>{lang === 'en' ? 'Demo' : 'Demostración'}</h2>
          <div className="demo-photos">
            <img src="/assets/demo.jpeg" alt="Demo 1" />
            <img src="/assets/demo_index.png" alt="Demo 2" />

          </div>
        </section>

        <div className="text-center mb-5">
          <button
            className="btn btn-highlight"
            onClick={() => setShowStartMessage(true)}
          >
            {lang === 'en' ? 'Start' : 'Comenzar'}
          </button>

          {showStartMessage && (
            <p className="alert alert-success mt-3">{t.startMessage}</p>
          )}
        </div>
      </main>

      <Footer />
    </div>
  );
}
