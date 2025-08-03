import Image from "next/image";

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">
            HTS Co-pilot
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            High Throughput Screening Analysis Platform
          </p>
          <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">
              🎯 Mission
            </h2>
            <p className="text-gray-700 mb-4">
              Transform 384-well plate experiment analysis from a day-long Excel process 
              into a 2-minute automated report with AI-powered insights.
            </p>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
              <div className="bg-blue-50 p-4 rounded-lg">
                <h3 className="font-semibold text-blue-800 mb-2">📊 Upload CSV</h3>
                <p className="text-sm text-blue-700">Upload your 384-well plate data</p>
              </div>
              <div className="bg-green-50 p-4 rounded-lg">
                <h3 className="font-semibold text-green-800 mb-2">⚡ AI Analysis</h3>
                <p className="text-sm text-green-700">Get instant statistical insights</p>
              </div>
              <div className="bg-purple-50 p-4 rounded-lg">
                <h3 className="font-semibold text-purple-800 mb-2">📈 Smart Report</h3>
                <p className="text-sm text-purple-700">Interactive results & recommendations</p>
              </div>
            </div>
          </div>
          
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-2xl font-semibold text-gray-800 mb-4">
              🚀 Deployment Status
            </h2>
            <div className="space-y-2">
              <div className="flex items-center justify-between p-3 bg-green-50 rounded-lg">
                <span className="font-medium text-green-800">✅ Sprint 0: Foundation</span>
                <span className="text-green-600">Complete</span>
              </div>
              <div className="flex items-center justify-between p-3 bg-yellow-50 rounded-lg">
                <span className="font-medium text-yellow-800">🔄 Deployment Pipeline</span>
                <span className="text-yellow-600">In Progress</span>
              </div>
              <div className="flex items-center justify-between p-3 bg-blue-50 rounded-lg">
                <span className="font-medium text-blue-800">📋 Sprint 1: Core Features</span>
                <span className="text-blue-600">Next</span>
              </div>
            </div>
          </div>
        </div>
        
        <div className="text-center text-gray-500">
          <p>Built with Next.js, FastAPI, and Claude Sonnet 4</p>
          <p className="text-sm mt-2">Target: &lt; 2 minutes end-to-end processing</p>
        </div>
      </div>
    </main>
  )
}
