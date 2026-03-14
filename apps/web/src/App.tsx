const pipelineSteps = [
  {
    title: "Bring in your restaurant data",
    description:
      "Upload sales, menu, recipe, and inventory data into a private workspace scoped to your restaurant only.",
  },
  {
    title: "Blend in local context",
    description:
      "Weather and neighborhood events add the demand signals that static spreadsheets miss.",
  },
  {
    title: "Forecast prep with less waste",
    description:
      "Generate dish-level guidance so teams prep closer to demand and throw away less food.",
  },
];

const trustPoints = [
  "Restaurant-specific forecasting workspace",
  "Weather and local events included in demand planning",
  "Prep decisions grounded in historical sales and recipes",
];

const metrics = [
  { value: "3", label: "core inputs", detail: "sales, weather, events" },
  { value: "1", label: "private tenant", detail: "each restaurant stays isolated" },
  { value: "24h", label: "planning horizon", detail: "daily prep recommendations" },
];

function App() {
  return (
    <div className="page-shell">
      <div className="ambient ambient-left" />
      <div className="ambient ambient-right" />

      <main className="layout">
        <section className="hero card">
          <div className="hero-copy">
            <p className="eyebrow">AI food waste forecasting</p>
            <h1>
              Forecast demand with your own restaurant data, not someone else&apos;s averages.
            </h1>
            <p className="lede">
              A restaurant-specific planning workspace that combines historical performance,
              local weather, and nearby events to help teams prep with less waste.
            </p>

            <div className="hero-actions">
              <a className="button button-primary" href="#workflow">
                View workflow
              </a>
              <a className="button button-secondary" href="#why-it-matters">
                Why it matters
              </a>
            </div>

            <ul className="trust-list">
              {trustPoints.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </div>

          <aside className="hero-panel">
            <div className="panel-header">
              <span className="panel-kicker">Forecast lens</span>
              <span className="panel-badge">restaurant scoped</span>
            </div>

            <div className="signal-grid">
              <article className="signal-card signal-card-accent">
                <p className="signal-label">Tonight</p>
                <strong>Rain + hockey game nearby</strong>
                <span>Expect sharper demand for delivery-friendly dishes.</span>
              </article>
              <article className="signal-card">
                <p className="signal-label">Tomorrow</p>
                <strong>Mild weather</strong>
                <span>Lower soup demand, higher salad and cold drink demand.</span>
              </article>
              <article className="signal-card">
                <p className="signal-label">Kitchen prep</p>
                <strong>Dish-level recommendations</strong>
                <span>Translate demand forecasts into prep quantities before service.</span>
              </article>
            </div>
          </aside>
        </section>

        <section className="metrics" aria-label="Product metrics">
          {metrics.map((metric) => (
            <article className="metric card" key={metric.label}>
              <p className="metric-value">{metric.value}</p>
              <p className="metric-label">{metric.label}</p>
              <p className="metric-detail">{metric.detail}</p>
            </article>
          ))}
        </section>

        <section className="story-grid" id="why-it-matters">
          <article className="card story-card">
            <p className="section-tag">Why this product</p>
            <h2>Food waste usually starts with weak planning inputs.</h2>
            <p>
              Most kitchens already know their teams, dishes, and rush patterns. What they lack
              is a clean system that pulls sales history together with outside demand drivers before
              prep decisions are made.
            </p>
          </article>

          <article className="card story-card story-card-highlight">
            <p className="section-tag">What makes it different</p>
            <h2>Each restaurant keeps its own data boundary.</h2>
            <p>
              The product is designed around tenant isolation. One restaurant&apos;s menu,
              historical sales, or forecasts never become another restaurant&apos;s training data.
            </p>
          </article>
        </section>

        <section className="workflow card" id="workflow">
          <div className="workflow-heading">
            <p className="section-tag">Workflow</p>
            <h2>How the homepage frames the product story</h2>
            <p>
              The interface should quickly explain the three things your users care about: what
              data they bring, what outside signals you add, and what operational decision they get
              back.
            </p>
          </div>

          <div className="workflow-steps">
            {pipelineSteps.map((step, index) => (
              <article className="step-card" key={step.title}>
                <span className="step-index">0{index + 1}</span>
                <h3>{step.title}</h3>
                <p>{step.description}</p>
              </article>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
