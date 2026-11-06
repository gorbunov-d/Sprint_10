import { defineConfig } from 'allure';

export default defineConfig({
  name: 'Sprint_10 — Яндекс.Маршруты',
  output: './allure-report',
  plugins: {
    awesome: {
      options: { singleFile: true, reportLanguage: 'ru' },
    },
  },
});
