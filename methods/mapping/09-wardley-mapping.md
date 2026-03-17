# Wardley Mapping

*Research compiled: 2026-02-23*

## Overview

Wardley Mapping is a strategic visualization technique that maps business components against a value chain (y-axis) and evolution axis (x-axis) to create situational awareness for decision-making. Created by Simon Wardley at Fotango in 2005, it provides a "topographical" view of business strategy — making the invisible visible and enabling purposeful, context-aware action.

Unlike traditional strategy frameworks that rely on stories or matrices, Wardley Maps show *where* components are positioned in their evolutionary journey and *how* they connect to deliver value, making strategic conversations visual, tangible, and challengeable.

## Historical Context

**Origins (2004-2005):** Simon Wardley developed Wardley Mapping while working at Fotango, initially creating the evolutionary framing in 2004 and the full mapping technique in 2005. The methodology emerged from his search to understand how to evaluate strategy, finding answers in military history and Sun Tzu's *The Art of War*.

**Development (2008-2010):** Further refined at Canonical UK, with components appearing in the 2010 "Better for Less" paper.

**Publishing (2017-2018):** Wardley published his comprehensive methodology in a series of 19 blog posts on Medium (collected as *Wardley Mapping* ebook), making it available under Creative Commons Attribution-ShareAlike 4.0 license — free for anyone to learn and use.

**Adoption (2015-present):** Gained significant traction within UK Government Digital Service (GDS) for strategic planning and digital service modernization, and increasingly adopted across enterprise architecture, product strategy, and technology organizations globally.

## Core Concepts

### The Fundamental Premise

**Everything evolves.** All capabilities, components, practices, and technologies follow a predictable evolutionary trajectory from novel wonder to commoditized ubiquity, driven by supply-and-demand competition. This evolution is inevitable, and understanding where components sit on this journey is essential for strategic decision-making.

### The Two Axes

**Y-Axis (Vertical): Value Chain / Visibility to User**
- Represents the value chain structure — how components depend on each other
- Higher components = more visible to end users
- Lower components = more abstracted, infrastructure-level
- Scaffolded by dependency relationships: "What does this need to work?"

**X-Axis (Horizontal): Evolution**
- Represents the evolutionary maturity of each component
- Left = less evolved (rare, uncertain, high-risk)
- Right = more evolved (common, standardized, low-risk)
- Movement is generally left-to-right over time

### The Four Stages of Evolution

All components evolve through four predictable stages:

**I. Genesis (Innovation/Novel)**
- Poorly understood, uncertain
- Rare, expensive, custom-built
- High failure rates
- Requires experimentation and exploration
- Examples: early AI research, novel user interfaces, breakthrough materials

**II. Custom-Built (Emerging)**
- Better understood, still uncertain
- Bespoke for specific contexts
- Evolving rapidly
- Requires skilled practitioners
- Examples: custom software solutions, specialized consulting services

**III. Product (Stabilizing)**
- Well-understood, fairly certain
- Off-the-shelf with some customization
- Feature competition emerges
- Increasingly standardized
- Examples: commercial software packages, branded services

**IV. Commodity (Mature/Utility)**
- Well-defined, very certain
- Standardized, volume operations
- Price competition dominates
- Essential but undifferentiated
- Examples: cloud computing, electricity, standard APIs

### The Strategy Cycle

Wardley Mapping integrates Sun Tzu's five factors of strategy with John Boyd's OODA loop:

**Purpose** — Why we're in the game (the first "why")

**Observe → Landscape** — Map the terrain, identify components and their positions

**Orient → Climate** — Understand forces acting on the landscape (how things move)

**Decide → Doctrine** — Apply universal principles for strategic success

**Act → Leadership** — Make the move (the second "why": why this move?)

This creates a continuous, adaptive cycle where strategy evolves through repeated iterations of mapping, sensing, deciding, and acting.

## Key Framework Elements

### Components

Any discrete element that provides value can be a component:
- Activities (customer service, software development)
- Practices (agile, design thinking)
- Data (customer information, analytics)
- Knowledge (domain expertise, methodologies)
- Technology (platforms, APIs, infrastructure)

Components are:
- **Anchored** by user needs (always at the top)
- **Positioned** according to visibility (y-axis) and evolution (x-axis)
- **Connected** by dependency lines showing what requires what

### Evolutionary Characteristics Cheatsheet

Wardley provides a detailed cheatsheet for determining evolutionary stage:

**Genesis:** Unique, novel, competitive advantage, high market differentiation, experimentation-focused, failure common, uncertain returns

**Custom:** Differentiating, bespoke solutions, artisan skills required, client-specific, learning-intensive, discovery-oriented

**Product:** Comparative advantage, good practices emerging, vendor relationships, feature competition, increasing ROI certainty

**Commodity:** Cost of deviation, operational excellence, volume operations, standardization, price competition, well-defined characteristics

### Situational Awareness

The core value of Wardley Mapping lies in creating **situational awareness** — a shared, visual understanding of:
- Who we serve (users)
- What they need (user needs)
- How we deliver (value chains)
- Where components are evolving (evolutionary positioning)
- What forces are acting (climatic patterns)
- What moves are available (gameplay patterns)

## Strategic Patterns

### Climatic Patterns

Components evolve and co-evolve in predictable ways:
- Evolution is driven by supply and demand competition
- Components move from left to right (genesis → commodity)
- Higher-order systems enable new genesis
- Inertia exists — organizations resist change
- Co-evolution occurs — one component's evolution affects others

### Doctrine (Universal Principles)

Wardley identifies 40+ universal principles for strategic success:
- Know your users
- Focus on user needs
- Use appropriate methods (different methods for different evolutionary stages)
- Think small (break down complexity)
- Remove bias and duplication
- Challenge assumptions
- Be transparent and open

### Forms of Gameplay (Strategic Moves)

Wardley identifies 61+ strategic plays, including:
- **Exploit evolution:** Use emerging commodities to create higher-order services
- **Create barriers:** Slow competitor evolution through patents, standards manipulation
- **Accelerate evolution:** Open source to commoditize competitors' revenue streams
- **Harvest/retire:** Extract value from declining components before exit
- **Future positioning:** Anticipate evolution and position ahead of the market

## Integration with Service Design & Business Architecture

### Service Design Synergies

**Complements Journey Mapping:** While customer journey maps show *sequence* and *emotional progression*, Wardley Maps show the *underlying system* of capabilities that enable each touchpoint and moment. They answer "what does it take to deliver this experience?"

**Informs Service Blueprinting:** Service blueprints detail frontstage/backstage activities; Wardley Maps add the evolutionary dimension — showing which backstage processes are commodities vs. differentiators, informing build/buy/partner decisions.

**Strategic Service Innovation:** By mapping the evolution of service components (channels, platforms, capabilities), service designers can identify opportunities to leverage commoditizing infrastructure to create new value at higher levels.

### Business Architecture Applications

**Capability Mapping Integration:** Business capability maps show *what* capabilities exist; Wardley Maps add *how evolved* each capability is, enabling strategic investment prioritization and maturity roadmapping.

**Value Stream Analysis:** Wardley Mapping provides evolutionary context for value streams, revealing where custom activities create genuine competitive advantage vs. where standardization and efficiency gains should dominate.

**Technology Architecture Alignment:** Maps bridge business strategy and technical architecture by showing how technology components (platforms, data, APIs) evolve and support business capabilities, informing architecture decisions and technical debt management.

**Portfolio Strategy:** For large enterprises, mapping product/service portfolios against evolution reveals where innovation investments should focus vs. where operational efficiency and cost reduction matter most.

### Architecture for Flow

Recent synthesis work (particularly Susanne Kaiser's *Architecture for Flow*, 2025) explicitly combines:
- **Wardley Mapping** for business strategy and landscape awareness
- **Domain-Driven Design (DDD)** for software architecture and boundaries
- **Team Topologies** for organizational design and communication patterns

This integration creates adaptive socio-technical systems optimized for fast flow of change — directly relevant to service design transformation and enterprise architecture modernization.

## Practical Applications

**Strategic Planning:** Replace or augment traditional planning with continuous mapping cycles that adapt to market evolution.

**Build vs. Buy Decisions:** Evolutionary positioning immediately reveals whether custom-building a component makes strategic sense (genesis/custom stages for differentiators) vs. buying/outsourcing (product/commodity stages for non-differentiators).

**Investment Allocation:** Map components across portfolios to guide R&D investment (genesis), platform investment (custom/product), and operational efficiency focus (commodity).

**Organizational Design:** Different evolutionary stages require different team cultures, management approaches, and operational models — maps inform org design.

**Risk Assessment:** Components on the left (genesis/custom) carry higher execution risk; components on the right (commodity) carry higher commoditization/disruption risk if you're trying to build business on them.

**Government Digital Services:** UK GDS extensively uses Wardley Mapping to identify modernization opportunities, avoid building what should be bought, and create strategic alignment across departments.

## Tools & Resources

**Official Resources:**
- [wardleymaps.com](https://www.wardleymaps.com/) — Simon Wardley's writings and glossary
- [learnwardleymapping.com](https://learnwardleymapping.com/) — Comprehensive guide and free ebook
- Medium series: "Wardleymaps" collection (19 chapters)
- Wardleypedia: Community-maintained wiki

**Online Mapping Tools:**
- OnlineWardleyMaps.com — Free, open-source mapping tool
- MapKeep — Dedicated Wardley mapping platform
- Miro templates — Collaborative whiteboard mapping
- VS Code extensions — Code-based mapping (MapScript)

**Key Texts:**
- *Wardley Mapping* by Simon Wardley (free, CC BY-SA 4.0)
- *Architecture for Flow* by Susanne Kaiser (2025) — Integration with DDD and Team Topologies

**Learning Resources:**
- #WardleyMaps community on Twitter/X
- Wardley Maps community on Slack
- Regular mapping meetups and conferences
- Government case studies from UK GDS

## Key Practitioners & Thought Leaders

**Simon Wardley** (Creator)
- Former CEO turned strategist
- Created methodology at Fotango, refined at Canonical
- Prolific speaker and writer
- Twitter/X: @swardley

**Ben Mosior**
- Compiled and maintains learnwardleymapping.com
- Created visual summaries and educational resources

**Susanne Kaiser**
- Author of *Architecture for Flow*
- Integrates Wardley Mapping with DDD and Team Topologies
- Focus on socio-technical systems

**Mark Thompson** (UK GDS)
- Championed adoption within UK government
- Focus on digital service modernization

**Will Larson** (*Staff Engineer* author)
- Uses Wardley Mapping for technology strategy
- Integration with engineering leadership practices

## Critical Perspectives

**Strengths:**
- Visual and tangible — makes strategy discussable
- Forces explicit assumptions that can be challenged
- Reveals dependencies and evolutionary dynamics often invisible in traditional frameworks
- Free and open methodology with strong community
- Applicable across business, product, technology, and organizational domains

**Critiques:**
- **Subjectivity:** Positioning components requires judgment; different mappers may place components differently
- **Assumption laundering:** Critics (e.g., Matt Edgar) warn maps can make assumptions *appear* factual when they're still hypotheses
- **Learning curve:** Takes practice to build good maps and interpret them effectively
- **Time investment:** Initial mapping can be time-consuming; may feel like overhead vs. "just deciding"
- **Over-simplification risk:** Complex situations may not fit neatly into four evolutionary stages

**Best Practices:**
- Treat maps as hypotheses, not truth — test assumptions against reality
- Map collaboratively to surface diverse perspectives and challenge groupthink
- Iterate frequently — maps are living artifacts, not one-time deliverables
- Start simple, add complexity only as needed
- Focus on actionable insights, not perfect positioning

## Connections to Other Frameworks

**Strategic Thinking:**
- Porter's Five Forces (competitive dynamics)
- Blue Ocean Strategy (value innovation)
- Ansoff Matrix (growth strategies)
- OODA Loop (adaptive decision-making)

**Design & Innovation:**
- Design Thinking (exploration in genesis stages)
- Lean Startup (experimentation and validation)
- Diffusion of Innovations (adoption and evolution)
- Technology Adoption Lifecycle (crossing the chasm)

**Enterprise Architecture:**
- TOGAF (architecture development method)
- Business Capability Modeling (what vs. how evolved)
- Value Stream Mapping (operational flow + evolution)
- ArchiMate (architecture visualization language)

**Organizational Design:**
- Team Topologies (team structures aligned to evolutionary stages)
- Conway's Law (org structure mirrors system architecture)
- Spotify Model (squads, tribes, chapters aligned to components)

## Future Directions

Wardley Mapping continues to evolve as a methodology:

**Increasing Enterprise Adoption:** More organizations (especially in tech and government) adopting mapping as core strategic practice

**Integration with Existing Frameworks:** Growing synthesis with DDD, Team Topologies, OKRs, and enterprise architecture frameworks

**Tooling Maturity:** Better software tools emerging for mapping, analysis, and collaboration

**AI and Automation:** Exploring AI-assisted mapping, pattern recognition, and strategic recommendations

**Education and Certification:** More formal training programs and mapping communities emerging globally

**Cross-Domain Applications:** Expanding beyond tech into healthcare, education, climate, and public policy

## Key Takeaways for Service Design & Architecture Practice

1. **Strategic Context for Service Components:** Map the capabilities underlying service delivery to understand which should be custom-built (differentiators) vs. commoditized (efficiency plays).

2. **Evolution-Aware Architecture:** Design service architectures that anticipate component evolution — plan for today's custom solution to become tomorrow's commodity.

3. **Portfolio Intelligence:** Use maps to guide service portfolio strategy, investment allocation, and innovation focus across multiple services.

4. **Shared Language:** Maps create visual artifacts for cross-functional alignment between service designers, architects, product managers, and executives.

5. **Continuous Strategy:** Replace annual planning theater with continuous mapping cycles that sense and respond to market evolution.

6. **Build-Operate-Transform:** Different components need different operating models — genesis needs experimentation, commodity needs operational excellence.

---

## Sources

- Wardley, Simon. *Wardley Mapping* (2018). Medium series compiled at [learnwardleymapping.com](https://learnwardleymapping.com/)
- Wikipedia: Wardley Map. [https://en.wikipedia.org/wiki/Wardley_map](https://en.wikipedia.org/wiki/Wardley_map)
- "A Strategy and Wardley Mapping Primer" (2025). [https://www.davesresearch.com/wardley-mapping/](https://www.davesresearch.com/wardley-mapping/)
- Kaiser, Susanne. *Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies* (2025). Addison-Wesley.
- Official Wardley Maps site: [https://www.wardleymaps.com/](https://www.wardleymaps.com/)
- UK Government Digital Service case studies on Wardley Mapping for digital transformation
- IT Revolution: "Using Wardley Mapping with the Value Flywheel" [https://itrevolution.com/articles/using-wardley-mapping-with-the-value-flywheel/](https://itrevolution.com/articles/using-wardley-mapping-with-the-value-flywheel/)
- Miro: "What are Wardley Maps?" [https://miro.com/blog/wardley-maps-whiteboard-canvas/](https://miro.com/blog/wardley-maps-whiteboard-canvas/)
