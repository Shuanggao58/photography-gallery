export default function HomePage() {
  return (
    <main className="container mx-auto px-4 py-8">
      <div className="text-center space-y-8">
        <div className="space-y-4">
          <h1 className="text-4xl md:text-6xl font-bold tracking-tight">
            Photography Gallery
          </h1>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            Welcome to a modern photography gallery built with Next.js, FastAPI, and PostgreSQL
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
          <div className="p-6 border rounded-lg">
            <h3 className="text-lg font-semibold mb-2">Frontend</h3>
            <p className="text-muted-foreground">
              Next.js 14 with TypeScript, Tailwind CSS, and Radix UI components
            </p>
          </div>
          
          <div className="p-6 border rounded-lg">
            <h3 className="text-lg font-semibold mb-2">Backend</h3>
            <p className="text-muted-foreground">
              FastAPI with SQLAlchemy, PostgreSQL, and AWS S3 integration
            </p>
          </div>
          
          <div className="p-6 border rounded-lg">
            <h3 className="text-lg font-semibold mb-2">Infrastructure</h3>
            <p className="text-muted-foreground">
              AWS services managed with Terraform and GitHub Actions CI/CD
            </p>
          </div>
        </div>

        <div className="space-y-4">
          <p className="text-muted-foreground">
            🚧 This gallery is currently under construction
          </p>
          <div className="flex justify-center space-x-4">
            <a
              href="/api/docs"
              className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-primary-foreground bg-primary hover:bg-primary/90"
            >
              View API Docs
            </a>
            <a
              href="https://github.com/Shuanggao58/photography-gallery"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center px-4 py-2 border border-input text-sm font-medium rounded-md text-foreground bg-background hover:bg-accent"
            >
              View on GitHub
            </a>
          </div>
        </div>
      </div>
    </main>
  )
}
