import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Photography Gallery',
  description: 'A modern photography gallery showcasing professional photography work',
  keywords: ['photography', 'gallery', 'portfolio', 'professional photos'],
  authors: [{ name: 'Your Name' }],
  openGraph: {
    title: 'Photography Gallery',
    description: 'A modern photography gallery showcasing professional photography work',
    type: 'website',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <div className="min-h-screen bg-background font-sans antialiased">
          {children}
        </div>
      </body>
    </html>
  )
}
