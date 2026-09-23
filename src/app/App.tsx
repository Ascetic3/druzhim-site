import { Header } from '../sections/Header';
import { Hero } from '../sections/Hero';
import {
  Activities,
  Audience,
  Contact,
  Director,
  Faq,
  Footer,
  FosterFamilies,
  Mission,
  Results,
  Season,
} from '../sections/HomeSections';

export function App() {
  return (
    <>
      <Header />
      <main id="main">
        <Hero />
        <Audience />
        <FosterFamilies />
        <Activities />
        <Season />
        <Mission />
        <Director />
        <Results />
        <Faq />
        <Contact />
      </main>
      <Footer />
    </>
  );
}
