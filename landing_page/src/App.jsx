import React, { useState } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';

const content = {
  en: {
     overview: `SignBridge is an innovative platform that connects the deaf and hearing communities through real-time sign language recognition and intelligent interpretation tools. Designed for web, mobile, and video conferencing platforms, it empowers inclusive communication anywhere.`,
    functionalities: [
      "AI-powered real-time sign language recognition",
      "Instant speech-to-sign translation",
      "Secure multi-user video conferencing with integrated sign support",
      "Support for multiple spoken and signed languages"
    ],
    vision: "To eliminate communication barriers and enable full inclusion through the power of technology.",
    mission: "To empower deaf and hearing individuals with seamless, intuitive, and inclusive communication tools.",
    teamNote: "This project was proudly presented on May 10 at the Mathematics Fair of the National University of Engineering.",
    startMessage: "Coming soon — the future of inclusive communication is near!"
  },
  es: {
     overview: `SignBridge es una plataforma innovadora que conecta a las comunidades sordas y oyentes mediante el reconocimiento en tiempo real del lenguaje de señas y herramientas inteligentes de interpretación. Diseñada para la web, móviles y plataformas de videoconferencia, permite una comunicación inclusiva en cualquier lugar.`,
    functionalities: [
      "Reconocimiento en tiempo real del lenguaje de señas impulsado por IA",
      "Traducción instantánea de voz a señas",
      "Videollamadas seguras con múltiples usuarios e interpretación integrada",
      "Soporte para múltiples lenguas habladas y de señas"
    ],
    vision: "Eliminar las barreras de comunicación y promover la inclusión total mediante la tecnología.",
    mission: "Empoderar a personas sordas y oyentes con herramientas de comunicación inclusivas, intuitivas y sin barreras.",
    teamNote: "Este proyecto fue presentado con orgullo el 10 de mayo en la Feria de Matemáticas de la Universidad Nacional de Ingeniería.",
    startMessage: "¡Muy pronto! El futuro de la comunicación inclusiva está cerca."
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
        {/* Overview */}
        <section className="overview-box mb-4">
          <h2>{lang === 'en' ? 'Overview' : 'Resumen'}</h2>
          <p>{t.overview}</p>
        </section>

        {/* Functionalities */}
        <section className="mb-4">
          <h2>{lang === 'en' ? 'Functionalities' : 'Funcionalidades'}</h2>
          <ul>
            {t.functionalities.map((func, i) => (
              <li key={i}>{func}</li>
            ))}
          </ul>
        </section>

        {/* Vision */}
        <section className="mb-4">
          <h2>{lang === 'en' ? 'Vision' : 'Visión'}</h2>
          <p>{t.vision}</p>
        </section>

        {/* Mission */}
        <section className="mb-4">
          <h2>{lang === 'en' ? 'Mission' : 'Misión'}</h2>
          <p>{t.mission}</p>
        </section>

        {/* Team */}
        <section className="mb-4">
          <h2>{lang === 'en' ? 'Team' : 'Equipo'}</h2>
          <div className="team-photos">
            <img src="/assets/team.jpg" alt="Team" />
            {/* Add more team photos as needed */}
          </div>
          <p className="team-note">{t.teamNote}</p>
        </section>

        {/* Demo */}
        <section className="mb-5">
          <h2>{lang === 'en' ? 'Demo' : 'Demostración'}</h2>
          <div className="demo-photos d-flex flex-wrap gap-3">
            <img src="/assets/demo.jpeg" alt="Demo 1" />
            <img src="/assets/demo_index.png" alt="Demo 2" />
          </div>
        </section>

        {/* Start Button */}
        <div className="text-center mb-5">
          <button
            className="btn btn-highlight"
            onClick={() => setShowStartMessage(true)}
          >
            {lang === 'en' ? 'Start' : 'Comenzar'}
          </button>

          {showStartMessage && (
            <p className="alert alert-success">{t.startMessage}</p>
          )}
        </div>
      </main>

      <Footer />
    </div>
  );
}
