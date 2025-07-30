/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    domains: ['your-bucket-name.s3.amazonaws.com'],
    formats: ['image/webp', 'image/avif'],
  },
  experimental: {
    optimizePackageImports: ['lucide-react'],
  },
}

module.exports = nextConfig
