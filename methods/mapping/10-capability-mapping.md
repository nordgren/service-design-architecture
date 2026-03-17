# Capability Mapping

**Research Date:** February 24, 2026  
**Phase:** 2 - Methods  
**Area:** Methods/Mapping  

## Overview

Business capability mapping is a foundational technique in enterprise and business architecture that provides a structured, stable view of **what** an organization does (or needs to do) to achieve its objectives—independent of **how** it does it (processes), **who** does it (organizational structure), or **which technologies** enable it.

A business capability map serves as a visual framework that illustrates the various capabilities of an organization and how they interrelate to support overall business objectives. It becomes a common language between business and IT, bridging strategy with architecture and execution.

## Core Definition

**Business Capability:** An ability that an organization possesses or needs to possess to achieve its objectives. Capabilities represent what the business does at a high level of abstraction.

Key characteristics:
- **Stable over time** — capabilities don't change as frequently as processes, systems, or org structures
- **Business-focused** — describes what the business does, not how
- **Technology-agnostic** — independent of specific applications or technical implementations
- **Outcome-oriented** — focused on delivering value

## Capability Hierarchy

### Levels of Granularity

Best practices recommend **2-3 levels** maximum to avoid excessive complexity:

1. **Level 1 (Top-level capabilities):** ~10 capabilities representing major domains
2. **Level 2 (Sub-capabilities):** Breakdown of top-level capabilities
3. **Level 3 (Detailed capabilities):** Further decomposition when needed (use sparingly)

**Example Hierarchy:**
```
Finance (Level 1)
├── Financial Planning & Analysis (Level 2)
│   ├── Budgeting (Level 3)
│   ├── Forecasting (Level 3)
│   └── Variance Analysis (Level 3)
├── Accounts Payable (Level 2)
└── Treasury Management (Level 2)
```

### Naming Conventions

According to the BIZBOK® Guide approach:
- Use **"business object – action"** naming convention
- Examples: "Customer Management," "Product Development," "Financial Reporting"
- Keep names clear, consistent, and business-oriented

## Capability Assessment Dimensions

### 1. Strategic Importance

**Key Question:** "Which capabilities are required to successfully deliver our strategy?"

**Assessment Metrics:**
- **Strategy Execution:** Is the capability required to achieve strategic goals?
- **Business/Operating Model:** Does the capability provide critical support for key value propositions?
- **Future Opportunity:** Does the capability support enhanced or new value propositions?

### 2. Maturity

**Key Question:** "Which capabilities are performing below expected levels?"

**Common Dimensions:**
- **People:** Skills, knowledge, training, culture
- **Process:** Efficiency, standardization, optimization
- **Technology:** Systems support, automation, integration
- **Information:** Data quality, availability, governance

**Maturity Scales:** Typically 1-5 rating:
- 1 = Immature/ad hoc
- 2 = Developing
- 3 = Defined
- 4 = Managed
- 5 = Optimized

### 3. Adaptability

**Key Question:** "Which capabilities are problematic to improve or change?"

**Assessment Metrics:**
- **Environmental Adaptability:** Response to external dynamics (regulations, market changes)
- **Customer Adaptability:** Response to changing customer needs
- **Capacity:** Ability to scale with demand

## Heat Mapping

### Purpose

Capability heat maps apply color-coding to visualize capability assessments, making patterns and priorities immediately apparent to stakeholders.

### Common Heat Map Types

1. **Maturity Heat Maps**
   - Green = Desired maturity level achieved
   - Yellow = One level below target
   - Red = Two or more levels below target
   - Purple = Capability doesn't exist yet

2. **Strategic Importance Heat Maps**
   - Visualize which capabilities are most critical to strategy
   - Guide investment prioritization

3. **Risk Heat Maps**
   - Show dependencies on underperforming technology
   - Identify single points of failure

4. **Cost/Investment Heat Maps**
   - Visualize spending across capabilities
   - Identify opportunities for rationalization

5. **Merger & Acquisition Heat Maps**
   - Compare capability maturity between acquiring firm and target
   - Identify integration opportunities and risks

### Creating Effective Heat Maps

**Process:**
1. Define assessment criteria (maturity, importance, risk, etc.)
2. Conduct surveys or use metrics to rate capabilities
3. Apply color scheme to visualize data
4. Generate different heat map views for different stakeholder perspectives

**Best Practice:** Different heat maps can be generated from the same capability map depending on the lens being applied—strategic, operational, technical, financial, etc.

## Capability-Based Planning (CBP)

### The CBP Cycle

A structured approach consisting of four phases:

1. **MAP** — Define and create the capability map
2. **ASSESS** — Measure capabilities against strategy and maturity
3. **PLAN** — Prioritize investments and improvements
4. **CONTROL** — Monitor execution and outcomes

### Strategic Portfolio Integration

Capability-based planning connects directly to strategic portfolio management by:

- **Linking investments to capabilities:** Every initiative should map to one or more capabilities
- **Prioritizing based on gaps:** Focus funding on capabilities that are strategically important but immature
- **Enabling scenario planning:** Model "what-if" scenarios for different investment strategies
- **Tracking capability improvement:** Measure ROI of initiatives in terms of capability maturity gains

### Integration Points

**Capability maps connect to:**
- **Value Streams:** Which capabilities enable key value flows
- **Applications/Systems:** Which technology supports each capability
- **Organizational Units:** Who owns and operates capabilities
- **Processes:** How capabilities are executed
- **People:** Skills and expertise required
- **Strategic Goals:** Which objectives capabilities support

## Best Practices

### Do's

✅ **Think present AND future:** Model capabilities you need now and will need tomorrow  
✅ **Involve cross-functional teams:** Engage diverse perspectives for accuracy  
✅ **Provide clear descriptions:** Don't just list capabilities—explain what each one means  
✅ **Focus on business needs first:** Let business challenges drive the model, not frameworks  
✅ **Keep it stable:** Capabilities should be relatively stable reference architecture  
✅ **Share early and often:** Make models visible across the organization  
✅ **Treat as living artifact:** Continuously update as business evolves  

### Don'ts

❌ **Go too deep:** Avoid over-complication—model only what provides insight  
❌ **Let capabilities overlap:** Core functionality should be distinct  
❌ **Make it static:** It's not a one-time deliverable  
❌ **Get stuck in nuance debates:** Good enough to start is better than perfect and never started  
❌ **Focus only on "as-is":** Include target/future-state capabilities  

## Common Use Cases

1. **IT Rationalization**
   - Map applications to capabilities
   - Identify redundant systems supporting the same capability
   - Prioritize decommissioning or consolidation

2. **Mergers & Acquisitions**
   - Compare capability maturity across organizations
   - Identify integration priorities and synergies
   - Plan post-merger operating model

3. **Digital Transformation**
   - Assess digital maturity across capabilities
   - Prioritize digitization investments
   - Track transformation progress

4. **Strategic Planning**
   - Link strategy to required capabilities
   - Identify capability gaps blocking strategic goals
   - Guide investment decisions

5. **Organizational Design**
   - Align organizational units to capabilities
   - Identify capability ownership issues
   - Support restructuring decisions

## Frameworks & Standards

### BIZBOK® (Business Architecture Body of Knowledge)

Published by the Business Architecture Guild, BIZBOK is the gold standard framework for business architecture, including comprehensive guidance on capability modeling. Often called "the ITIL of business architecture."

**Key Contributions:**
- Standardized capability definitions
- Common reference models
- Capability-based planning methodology
- Integration with value streams and business models

### TOGAF (The Open Group Architecture Framework)

TOGAF's Business Architecture phase includes detailed guidance on capability modeling as part of enterprise architecture practice.

**Key Contributions:**
- Capability modeling within ADM cycle
- Heat mapping techniques
- Integration with other architecture domains
- Capability-based planning approach

### ArchiMate®

ArchiMate provides a visual modeling language that includes business capability as a core element, enabling integration with processes, applications, and technology architecture.

## Tools & Platforms

### Leading EA Tools Supporting Capability Mapping:

- **Ardoq** — Cloud-native, graph-based, people-centric approach
- **Bizzdesign Horizzon** — Comprehensive EA suite with advanced capability assessment
- **LeanIX** — SaaS EA platform with strong capability modeling
- **Sparx Systems Enterprise Architect** — Modeling tool with ArchiMate support
- **BOC ADOIT** — EA management with capability portfolio management
- **Avolution ABACUS** — Strategy-to-execution platform
- **Planview** — Strategic portfolio management with capability integration

### Key Tool Features:

- Visual capability hierarchy editing
- Heat map generation
- Assessment/scoring workflows
- Application/system mapping
- Impact analysis
- Integration with strategic planning
- Stakeholder surveys and data collection
- Presentation and sharing capabilities

## Notable Practitioners & Thought Leaders

### Organizations:

- **The Open Group** — TOGAF framework stewardship
- **Business Architecture Guild** — BIZBOK development and certification
- **Gartner** — Research and advisory on capability modeling
- **Forrester** — Enterprise architecture research

### Vendor Thought Leaders:

- **Ardoq** — Focus on data-driven, people-centric capability modeling
- **Bizzdesign** — Capability-based planning methodology
- **LeanIX** — SaaS delivery and continuous architecture
- **North Highland** — Consulting expertise in capability-based transformation

### Academic & Research:

- **Svyatoslav Kotusev** — EA research, including empirical studies on capability modeling practices
- Research into how organizations actually use capability models (vs. prescribed frameworks)

## Assessment Frameworks

### VRINS Framework for Capability Assessment

Used to evaluate strategic value of capabilities:

- **Valuable:** Does it raise revenues or lower costs?
- **Rare:** Is it unique among organizations?
- **Inimitable:** Can it be copied by competitors?
- **Non-Substitutable:** Can other capabilities provide the same functionality?
- **Sustainable:** Can it scale and repeat over time?

### Capability Maturity Models

Multiple approaches exist:

1. **Custom Maturity Models:** Defined per organization
2. **CMMI-style:** Process maturity orientation
3. **Multi-dimensional:** Assessing People, Process, Technology, Information separately
4. **Balanced Scorecard:** Multiple perspectives (financial, customer, internal, learning)

## Connection to Service Design

While capability mapping originates from enterprise architecture, it increasingly intersects with service design:

- **Service Capabilities:** The abilities needed to deliver and support services
- **Service Blueprinting Integration:** Mapping capabilities to frontstage/backstage activities
- **Journey-to-Capability Mapping:** Linking customer journey stages to enabling capabilities
- **Value Stream Alignment:** Connecting capabilities to end-to-end value delivery

This convergence represents the **intersection of outside-in (service design) and inside-out (enterprise architecture)** perspectives—a core theme in modern transformation approaches.

## Key Takeaways

1. **Capability mapping provides stable reference architecture** — more stable than processes, org charts, or technology
2. **Heat maps make capability assessments actionable** — visual tools for executive decision-making
3. **Assessment requires multiple dimensions** — strategic importance, maturity, and adaptability
4. **CBP connects strategy to execution** — bridges the gap between boardroom and implementation
5. **Integration is power** — linking capabilities to applications, people, value streams unlocks insights
6. **Living artifact, not static deliverable** — must evolve with the business
7. **Common language for business and IT** — reduces translation errors in digital transformation

## Sources

- **TOGAF® Standard, Business Architecture Guide** — The Open Group  
  https://pubs.opengroup.org/togaf-standard/business-architecture/business-capabilities.html

- **"Business Capability Model: A Guide to Benefits and Best Practices"** — Ardoq (2024)  
  https://www.ardoq.com/knowledge-hub/business-capability-modeling

- **"Capability-Based Planning: How to Assess and Improve Business Capabilities"** — Bizzdesign (2026)  
  https://bizzdesign.com/blog/an-approach-how-to-assess-business-capabilities

- **"8 Steps to Effective Capability-Based Planning"** — North Highland (2025)  
  https://northhighland.com/insights/guides/8-steps-to-effective-capability-based-planning

- **"How to Create a Business Capability Map, Examples & Templates"** — Avolution  
  https://www.avolutionsoftware.com/our-resources/how-to-create-a-business-capability-map/

- **"Business Capability Maps: Current Practices and Use Cases for Enterprise Architecture Management"** — Research (2018)  
  https://www.researchgate.net/publication/323378815

- **BIZBOK® Guide** — Business Architecture Guild  
  (Membership required for full access)

- **"Strategic Portfolio Management Capabilities Guide"** — Planview  
  https://success.planview.com/

---

*This research note is part of the Service Design × Business Architecture knowledge base initiative.*
