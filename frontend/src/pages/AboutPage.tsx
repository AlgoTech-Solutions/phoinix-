import { PageHeader } from '../components/Layout'

export default function AboutPage() {
  return (
    <div className="max-w-4xl mx-auto">
      <PageHeader title="About Us" />
      <div className="mt-8 rounded-2xl border border-white/10 bg-white/[0.02] p-8 backdrop-blur-xl shadow-2xl relative overflow-hidden">
        <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-fuchsia-400 via-pink-400 to-violet-500" />
        <div className="space-y-6 text-fuchsia-100/70 text-lg leading-relaxed">
          <p className="font-medium text-white text-xl">
            Welcome to Project Phoenix AI
          </p>
          <p>
            Project Phoenix is an advanced AI-powered YouTube management platform designed to automate and elevate your content creation workflow. Our system integrates cutting-edge research, intelligent scriptwriting, seamless voiceovers, and dynamic editing into a unified, glass-morphic command center.
          </p>
          <p>
            This project was brought to life by <strong className="text-fuchsia-300">Team Cipher</strong>. We are a dedicated group of innovators and developers passionate about building state-of-the-art tools that empower creators to reach their maximum potential.
          </p>
          <div className="mt-8 pt-8 border-t border-white/10 flex items-center gap-4">
            <div className="flex h-12 w-12 items-center justify-center rounded-xl border border-fuchsia-200/20 bg-fuchsia-400/10 text-2xl shadow-[0_0_15px_rgba(239,159,232,0.15)]">
              ✦
            </div>
            <div>
              <p className="text-white font-bold tracking-wide">Team Cipher</p>
              <p className="text-sm text-fuchsia-200/50">Innovating the future of content</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
