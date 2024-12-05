import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <SidebarProvider>
      <AppSidebar />
        <SidebarTrigger />
          <App />
    </SidebarProvider>
  </StrictMode>
)
