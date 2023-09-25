import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  base: "/https://github.com/beedev-services/hiveMentor/chat_client/",
  plugins: [react()],
})
