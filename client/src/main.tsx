import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { ThemeProvider } from "@/components/theme-provider"
import { AppSidebar } from "@/components/app-sidebar"
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ThemeProvider defaultTheme='dark' storageKey='vite-ui-theme'>
      <SidebarProvider>
        <AppSidebar />
          <SidebarTrigger />
            <App />
      </SidebarProvider>
    </ThemeProvider>
  </StrictMode>
)
