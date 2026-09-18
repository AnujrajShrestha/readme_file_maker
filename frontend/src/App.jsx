import { useMemo, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import {
  ArrowRight,
  Check,
  Clipboard,
  ExternalLink,
  LoaderCircle,
  Sparkles,
  Terminal,
  WandSparkles,
  AlertCircle,
  RotateCcw,
  GitBranch,
} from "lucide-react";
import AnimatedBackground from "./components/AnimatedBackground";

const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

const initialForm = {
  url: "",
  project_name: "",
  author_name: "",
  github_id_url: "",
};

function getReadmeText(response) {
  if (!response) return "";
  if (typeof response === "string"){
      return respose
  }
  return response.readme || " ";
}

function App() {
  const [form, setForm] = useState(initialForm);
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);

  const readme = useMemo(() => getReadmeText(response),[response]);

  const update = (key, value) => setForm((current) => ({ ...current, [key]: value }));

  const generate = async (event) => {
    event.preventDefault();
    setError("");
    setResponse(null);
    setCopied(false);
    setLoading(true);

    try {
      const res = await fetch(`${API_URL}/maker`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) {
        throw new Error(data.detail || `Request failed with status ${res.status}`);
      }
      setResponse(data);
      setTimeout(() => document.getElementById("result")?.scrollIntoView({ behavior: "smooth" }), 50);
    } catch (err) {
      setError(err.message || "Could not connect to the backend.");
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setForm(initialForm);
    setResponse(null);
    setError("");
    setCopied(false);
  };

  const copyReadme = async () => {
    const text = readme || JSON.stringify(response?.result ?? response, null, 2);
    await navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 1600);
  };

  return (
    <div className="min-h-screen overflow-x-hidden">
      <AnimatedBackground />

      <header className="mx-auto flex max-w-6xl items-center justify-between px-5 py-5 sm:px-8">
        <a href="#" className="flex items-center gap-2.5">
          <span className="grid size-9 place-items-center rounded-xl bg-indigo-500/15 ring-1 ring-indigo-400/25">
            <WandSparkles className="size-5 text-indigo-300" />
          </span>
          <span className="font-bold tracking-tight text-slate-100">README<span className="text-indigo-400">Forge</span></span>
        </a>

        <a
          href="https://github.com/AnujrajShrestha/readme_file_maker"
          target="_blank"
          rel="noreferrer"
          className="flex items-center gap-2 rounded-full border border-white/10 bg-white/[.03] px-3.5 py-2 text-sm text-slate-300 transition hover:border-white/20 hover:bg-white/[.06] hover:text-white"
        >
          <GitBranch className="size-4" />
          <span className="hidden sm:inline">Repository</span>
        </a>
      </header>

      <main className="mx-auto max-w-6xl px-5 pb-20 pt-12 sm:px-8 sm:pt-20">
        <section className="mx-auto max-w-4xl text-center">
          <div className="mb-5 inline-flex items-center gap-2 rounded-full border border-indigo-400/20 bg-indigo-400/8 px-3.5 py-1.5 text-xs font-medium text-indigo-200">
            <Sparkles className="size-3.5" />
            AI-powered README generation
          </div>

          <h1 className="text-4xl font-black tracking-tight text-white sm:text-6xl lg:text-7xl">
            Turn a GitHub repo into a
            <span className="block bg-gradient-to-r from-indigo-300 via-violet-300 to-cyan-300 bg-clip-text text-transparent">
              polished README.
            </span>
          </h1>

          <p className="mx-auto mt-6 max-w-2xl text-base leading-7 text-slate-400 sm:text-lg">
            Give the AI your repository and author details. The FastAPI backend analyzes the project and returns README content ready to use.
          </p>
        </section>

        <section className="mx-auto mt-12 max-w-3xl">
          <form onSubmit={generate} className="glass rounded-3xl p-5 sm:p-7">
            <div className="mb-7 flex items-center justify-between gap-4">
              <div>
                <p className="text-sm font-semibold text-white">Project details</p>
                <p className="mt-1 text-xs text-slate-500">All fields are sent to <code className="text-indigo-300">POST /maker</code>.</p>
              </div>
              <div className="hidden items-center gap-2 rounded-full bg-emerald-400/8 px-3 py-1.5 text-xs text-emerald-300 sm:flex">
                <span className="size-1.5 rounded-full bg-emerald-400" />
                Backend ready
              </div>
            </div>

            <div className="space-y-4">
              <Field label="GitHub repository URL" icon={<GitBranch className="size-4" />} value={form.url} onChange={(e) => update("url", e.target.value)} placeholder="https://github.com/username/project" required type="url" />
              <div className="grid gap-4 sm:grid-cols-2">
                <Field label="Project name" icon={<Terminal className="size-4" />} value={form.project_name} onChange={(e) => update("project_name", e.target.value)} placeholder="My Awesome Project" required />
                <Field label="Author name" icon={<Sparkles className="size-4" />} value={form.author_name} onChange={(e) => update("author_name", e.target.value)} placeholder="Your Name" required />
              </div>
              <Field label="Author GitHub URL" icon={<ExternalLink className="size-4" />} value={form.github_id_url} onChange={(e) => update("github_id_url", e.target.value)} placeholder="https://github.com/username" required type="url" />
            </div>

            {error && (
              <div className="mt-5 flex gap-3 rounded-2xl border border-red-400/20 bg-red-400/8 p-4 text-sm text-red-200">
                <AlertCircle className="mt-0.5 size-4 shrink-0" />
                <div>
                  <p className="font-semibold">Generation failed</p>
                  <p className="mt-1 text-red-200/70">{error}</p>
                </div>
              </div>
            )}

            <button
              disabled={loading}
              className="mt-6 flex w-full items-center justify-center gap-2 rounded-2xl bg-indigo-500 px-5 py-3.5 font-semibold text-white shadow-lg shadow-indigo-500/15 transition hover:bg-indigo-400 disabled:cursor-not-allowed disabled:opacity-60"
            >
              {loading ? <><LoaderCircle className="size-5 animate-spin" /> Analyzing repository...</> : <>Generate README <ArrowRight className="size-4" /></>}
            </button>

            <p className="mt-4 text-center text-[11px] text-slate-600">
              Make sure your FastAPI server is running at {API_URL}
            </p>
          </form>
        </section>

        {response && (
          <section id="result" className="mx-auto mt-12 max-w-5xl scroll-mt-8">
            <div className="mb-5 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
              <div>
                <div className="mb-2 inline-flex items-center gap-2 text-xs font-medium text-emerald-300">
                  <Check className="size-4" /> README generated successfully
                </div>
                <h2 className="text-2xl font-bold text-white sm:text-3xl">{response.project_name}</h2>
                <a href={response.repository_url} target="_blank" rel="noreferrer" className="mt-1 inline-flex items-center gap-1 text-sm text-slate-500 hover:text-indigo-300">
                  {response.repository_url} <ExternalLink className="size-3" />
                </a>
              </div>

              <div className="flex gap-2">
                <button onClick={copyReadme} className="flex items-center gap-2 rounded-xl border border-white/10 bg-white/[.04] px-3.5 py-2 text-sm text-slate-300 hover:bg-white/[.08]">
                  {copied ? <Check className="size-4 text-emerald-400" /> : <Clipboard className="size-4" />}
                  {copied ? "Copied" : "Copy README"}
                </button>
                <button onClick={reset} className="flex items-center gap-2 rounded-xl border border-white/10 bg-white/[.04] px-3.5 py-2 text-sm text-slate-300 hover:bg-white/[.08]">
                  <RotateCcw className="size-4" /> New
                </button>
              </div>
            </div>

            <div className="glass overflow-hidden rounded-3xl">
              {readme ? (
                <article className="prose-readme p-6 sm:p-9">
                <ReactMarkdown remarkPlugins={[remarkGfm]}>
                  {readme}
                </ReactMarkdown>
                </article>
            ) : (
                <div className="p-8 text-center text-slate-400">
                  README content was not returned by the backend.
                </div>
            )}
            </div>
          </section>
        )}
      </main>

      <footer className="mx-auto max-w-6xl border-t border-white/5 px-5 py-8 text-center text-xs text-slate-600 sm:px-8">
        READMEForge · React + Vite + Tailwind CSS · FastAPI backend
      </footer>
    </div>
  );
}

function Field({ label, icon, ...props }) {
  return (
    <label className="block">
      <span className="mb-2 flex items-center gap-2 text-xs font-medium text-slate-400">
        {icon} {label}
      </span>
      <input
        {...props}
        className="w-full rounded-2xl border border-white/10 bg-black/20 px-4 py-3.5 text-sm text-white outline-none placeholder:text-slate-600 transition focus:border-indigo-400/50 focus:ring-4 focus:ring-indigo-500/10"
      />
    </label>
  );
}

export default App;