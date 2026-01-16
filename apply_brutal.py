#!/usr/bin/env python3
import re

# Read the file
with open('/home/user/dfw/index-beton.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and extract the style block
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if not style_match:
    print("Style block not found!")
    exit(1)

old_style = style_match.group(1)

# Create BRUTAL style
brutal_style = """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@500;600&display=swap');

/* BRUTAL RESET - NO ROUNDNESS */
* {
  border-radius: 0 !important;
}

/* CONCRETE TEXTURE BACKGROUND */
body {
  font-family: 'Inter', Arial, Helvetica, sans-serif !important;
  font-weight: 600 !important;
  letter-spacing: -0.01em !important;
  overflow: hidden;
  background: repeating-linear-gradient(
    0deg,
    #565656,
    #565656 2px,
    #5a5a5a 2px,
    #5a5a5a 4px
  ) !important;
  position: relative;
}

/* DIRECTIONAL LIGHT EFFECT */
body::before {
  content: "";
  position: fixed;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(
    45deg,
    transparent 40%,
    rgba(255, 255, 255, 0.15) 50%,
    transparent 60%
  );
  pointer-events: none;
  z-index: 999999;
}

@media (max-width:768px){
  body{
    padding:0 !important;
    background: repeating-linear-gradient(
      0deg,
      #565656,
      #565656 2px,
      #5a5a5a 2px,
      #5a5a5a 4px
    ) !important;
  }
}

/* BRUTAL TYPOGRAPHY - HEADINGS */
h1, h2, h3, h4, h5, h6,
#circular-sidebar-title,
.sidebar-link-name,
.circular-item-name,
.mobile-app-icon-name,
.mobile-dock-icon-name,
#mobile-folder-title,
#current-folder-title {
  font-family: 'Space Grotesk', Arial, sans-serif !important;
  font-weight: 700 !important;
  letter-spacing: -0.02em !important;
  text-transform: uppercase !important;
}

/* BRUTAL SCROLLBAR */
::-webkit-scrollbar {
  width: 12px !important;
  height: 12px !important;
  background: #4a4a4a;
}

::-webkit-scrollbar-track {
  background: #2a2a2a !important;
  border: 2px solid #1a1a1a !important;
}

::-webkit-scrollbar-thumb {
  background: #6b6b6b !important;
  border: 2px solid #2a2a2a !important;
  border-radius: 0 !important;
}

::-webkit-scrollbar-thumb:hover {
  background: #1a1a1a !important;
}

#sidebar-scroll-wrapper::-webkit-scrollbar {
  width: 12px !important;
  background: #4a4a4a;
}

#sidebar-scroll-wrapper::-webkit-scrollbar-track {
  background: #2a2a2a !important;
  border: 2px solid #1a1a1a !important;
}

#sidebar-scroll-wrapper::-webkit-scrollbar-thumb {
  background: #6b6b6b !important;
  border: 2px solid #2a2a2a !important;
  border-radius: 0 !important;
}

#sidebar-scroll-wrapper::-webkit-scrollbar-thumb:hover {
  background: #1a1a1a !important;
}

/* BRUTAL HARD SHADOWS */
.file-item, .gallery-thumb-item, .desktop-item {
  box-shadow: 8px 8px 0 rgba(0, 0, 0, 0.3) !important;
  transition: none !important;
}

.finder-window {
  box-shadow: 12px 12px 0 rgba(0, 0, 0, 0.4) !important;
  border: 3px solid #2a2a2a !important;
}

/* MONOCHROME BRUTAL COLORS */
.file-item.selected>div {
  background-color: #6b6b6b !important;
  outline: 3px solid #2a2a2a !important;
}

.file-item.selected>p {
  background-color: #4a4a4a !important;
  color: white !important;
}

.list-view .file-item.selected {
  background-color: #4a4a4a !important;
}

.gallery-thumb-item.selected {
  background-color: #6b6b6b !important;
  outline: 3px solid #2a2a2a !important;
}

.desktop-item.selected>p {
  background-color: #4a4a4a !important;
  color: white !important;
  text-shadow: none !important;
}

#minimized-icon-container.selected>p {
  background-color: #4a4a4a !important;
  color: white !important;
  text-shadow: none !important;
}

.dragging {
  user-select: none;
  cursor: grabbing !important;
  opacity: 0.8;
  transition: none !important;
}

.resizing {
  user-select: none;
  transition: none !important;
}

/* BRUTAL WINDOW CONTROLS */
.window-control {
  width: 12px;
  height: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #2a2a2a !important;
}

.window-control.close {
  background-color: #4a4a4a !important;
}

.window-control.close:hover {
  background-color: #1a1a1a !important;
}

.window-control.maximize {
  background-color: #6b6b6b !important;
}

.window-control.maximize:hover {
  background-color: #4a4a4a !important;
}

.resize-handle {
  position: absolute;
  z-index: 1;
}

.resize-handle[data-direction="n"]{top:-3px;left:6px;right:6px;height:6px;cursor:n-resize}
.resize-handle[data-direction="s"]{bottom:-3px;left:6px;right:6px;height:6px;cursor:s-resize}
.resize-handle[data-direction="w"]{top:6px;bottom:6px;left:-3px;width:6px;cursor:w-resize}
.resize-handle[data-direction="e"]{top:6px;bottom:6px;right:-3px;width:6px;cursor:e-resize}
.resize-handle[data-direction="nw"]{top:-3px;left:-3px;width:12px;height:12px;cursor:nw-resize}
.resize-handle[data-direction="ne"]{top:-3px;right:-3px;width:12px;height:12px;cursor:ne-resize}
.resize-handle[data-direction="sw"]{bottom:-3px;left:-3px;width:12px;height:12px;cursor:sw-resize}
.resize-handle[data-direction="se"]{bottom:-3px;right:-3px;width:12px;height:12px;cursor:se-resize}

.pdf-canvas-container {
  background-color: #6b6b6b !important;
}

.pdf-canvas-container canvas {
  box-shadow: 8px 8px 0 rgba(0,0,0,0.3) !important;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #4a4a4a !important;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  z-index: 10;
}

.loading-text {
  font-size: 18px;
  margin-bottom: 10px;
  color: #ffffff;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}

.loading-progress {
  width: 200px;
  height: 6px;
  background-color: #2a2a2a !important;
  overflow: hidden;
  border: 2px solid #1a1a1a !important;
}

.progress-bar {
  height: 100%;
  background-color: #6b6b6b !important;
  width: 0%;
  transition: none !important;
}

/* MOBILE INTERFACE BRUTAL */
@media (max-width:768px){
  .finder-window,#desktop-icons,#minimized-icon-container,#window-container{display:none !important}
  #mobile-interface{display:flex !important}
}

#mobile-interface {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  height: 100dvh;
  flex-direction: column;
  background: transparent;
  z-index: 9999;
  overflow: hidden;
  font-family: 'Inter', Arial, sans-serif !important;
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
  box-sizing: border-box;
}

#mobile-status-bar {
  flex-shrink: 0;
  height: 4%;
  min-height: 24px;
  max-height: 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 5%;
  color: white;
  font-size: clamp(10px,2.5vw,14px);
  font-weight: 700;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.5);
  letter-spacing: -0.02em;
  text-transform: uppercase;
}

#mobile-main-area{flex:1;position:relative;overflow:hidden;display:flex;flex-direction:column;padding:1% 2%;min-height:0}
#mobile-pages-container{flex:1;position:relative;overflow:hidden;min-height:0}
#mobile-pages-wrapper{display:flex;height:100%;transition:none !important;touch-action:pan-y pinch-zoom}
.mobile-page{flex-shrink:0;width:100%;height:100%;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(6,1fr);gap:2%;padding:1%;box-sizing:border-box;align-items:center;justify-items:center}

.mobile-app-icon {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  overflow: hidden;
}

/* BRUTAL ICON CONTAINER WITH NOISE */
.mobile-app-icon-image {
  --icon-size: min(18vw,calc((100dvh - 20%) / 8));
  width: calc(var(--icon-size) * 0.9);
  height: calc(var(--icon-size) * 0.9);
  aspect-ratio: 1 / 1;
  background: #4a4a4a !important;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  box-shadow: 8px 8px 0 rgba(0,0,0,0.3) !important;
  transition: none !important;
  flex-shrink: 0;
  border: 3px solid #2a2a2a !important;
  position: relative;
}

.mobile-app-icon-image::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' /%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.3'/%3E%3C/svg%3E");
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1;
}

.mobile-app-icon-image:active {
  box-shadow: 4px 4px 0 rgba(0,0,0,0.4) !important;
  transform: translate(4px, 4px);
}

.mobile-app-icon-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: grayscale(0.9) contrast(1.3) !important;
  mix-blend-mode: multiply;
}

.mobile-app-icon-image svg {
  width: 50%;
  height: 50%;
  flex-shrink: 0;
  filter: grayscale(0.9) contrast(1.3) !important;
}

.mobile-app-icon-name {
  margin-top: 3px;
  font-size: clamp(8px,2vw,11px);
  color: white;
  text-align: center;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.5);
  text-overflow: ellipsis;
  white-space: nowrap;
  width: var(--icon-size,18vw);
  font-weight: 700;
  line-height: 1.4;
  padding-bottom: 2px;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}

#mobile-page-dots{display:none;align-items:center;gap:6px;padding:1% 0;height:3%;min-height:16px}
.mobile-page-dot{width:6px;height:6px;background:#6b6b6b;transition:none !important}
.mobile-page-dot.active{background:#1a1a1a;transform:scale(1.2)}

#mobile-dock {
  flex-shrink: 0;
  height: 11%;
  min-height: 70px;
  max-height: 100px;
  padding: 1% 3% 3%;
  display: flex;
  justify-content: center;
  align-items: center;
}

#mobile-dock-container {
  background: #4a4a4a !important;
  padding: 8px 12px;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  width: 92%;
  max-width: 380px;
  box-shadow: 8px 8px 0 rgba(0,0,0,0.3) !important;
  border: 3px solid #2a2a2a !important;
  font-size: 0 !important;
  line-height: 0 !important;
  gap: 4px;
}

.mobile-dock-icon{font-size:0 !important;display:flex;flex-direction:column;align-items:center;justify-content:center;cursor:pointer;-webkit-tap-highlight-color:transparent;flex:1;max-width:20%}

.mobile-dock-icon-image {
  font-size: 0 !important;
  --dock-icon-size: min(14vw,52px);
  width: calc(var(--dock-icon-size) * 0.9);
  height: calc(var(--dock-icon-size) * 0.9);
  aspect-ratio: 1 / 1;
  background: #6b6b6b !important;
  transition: none !important;
  border: 3px solid #2a2a2a !important;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  box-shadow: 4px 4px 0 rgba(0,0,0,0.3) !important;
  flex-shrink: 0;
}

.mobile-dock-icon.active .mobile-dock-icon-image {
  background: #1a1a1a !important;
  border-color: #ffffff !important;
}

.mobile-dock-icon-image:active {
  box-shadow: 2px 2px 0 rgba(0,0,0,0.4) !important;
  transform: translate(2px, 2px);
}

.mobile-dock-icon-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: grayscale(0.9) contrast(1.3) !important;
  mix-blend-mode: multiply;
}

.mobile-dock-icon-image svg{width:55%;height:55%;flex-shrink:0;filter:grayscale(0.9) contrast(1.3) !important}

.mobile-dock-icon-name {
  font-size: clamp(7px,1.8vw,9px) !important;
  line-height: 1.4 !important;
  margin-top: 3px;
  color: white;
  text-align: center;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.5);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 100%;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}

#mobile-folder-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.7) !important;
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 10000;
  opacity: 0;
  transition: none !important;
}

#mobile-folder-overlay.visible{opacity:1}

#mobile-folder-container {
  width: 80%;
  max-width: min(350px,80vw);
  aspect-ratio: 1 / 1.1;
  max-height: 70dvh;
  background: #6b6b6b !important;
  padding: 4%;
  display: flex;
  flex-direction: column;
  transition: none !important;
  box-sizing: border-box;
  cursor: grab;
  user-select: none;
  border: 3px solid #2a2a2a !important;
  box-shadow: 12px 12px 0 rgba(0,0,0,0.4) !important;
}

#mobile-folder-header{flex-shrink:0;display:flex;align-items:center;justify-content:center;position:relative;margin-bottom:3%}
#mobile-folder-back-btn{position:absolute;left:0;width:32px;height:32px;display:flex;align-items:center;justify-content:center;cursor:pointer;-webkit-tap-highlight-color:transparent;color:#1a1a1a;transition:none !important}
#mobile-folder-back-btn:active{transform:translate(2px,2px)}
#mobile-folder-back-btn svg{width:20px;height:20px}

#mobile-folder-title {
  font-size: clamp(14px,4vw,18px);
  font-weight: 700;
  color: #1a1a1a;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}

#mobile-folder-pages-wrapper{flex:1;overflow:hidden;position:relative;min-height:0}
#mobile-folder-pages{display:flex;height:100%;transition:none !important}
.mobile-folder-page{flex-shrink:0;width:100%;height:100%;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:4%;padding:2%;box-sizing:border-box;align-items:center;justify-items:center}
.mobile-folder-icon{display:flex;flex-direction:column;align-items:center;justify-content:center;cursor:pointer;width:100%;height:100%;overflow:hidden}

.mobile-folder-icon-image {
  --folder-icon-size: min(18vw,56px);
  width: calc(var(--folder-icon-size) * 0.9);
  height: calc(var(--folder-icon-size) * 0.9);
  aspect-ratio: 1 / 1;
  background: #4a4a4a !important;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  transition: none !important;
  flex-shrink: 0;
  border: 3px solid #2a2a2a !important;
  box-shadow: 6px 6px 0 rgba(0,0,0,0.3) !important;
}

.mobile-folder-icon-image:active {
  box-shadow: 3px 3px 0 rgba(0,0,0,0.4) !important;
  transform: translate(3px, 3px);
}

.mobile-folder-icon-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: grayscale(0.9) contrast(1.3) !important;
}

.mobile-folder-icon-image svg{width:50%;height:50%;flex-shrink:0;filter:grayscale(0.9) contrast(1.3) !important}

.mobile-folder-icon-name {
  margin-top: 3px;
  font-size: clamp(8px,2vw,10px);
  color: #1a1a1a;
  text-align: center;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: var(--folder-icon-size,56px);
  line-height: 1.4;
  padding-bottom: 2px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}

#mobile-folder-dots{display:flex;justify-content:center;align-items:center;gap:6px;padding:8px 0 4px}
.mobile-folder-dot{width:6px;height:6px;background:#4a4a4a;transition:none !important}
.mobile-folder-dot.active{background:#1a1a1a}

#mobile-app-viewer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.7) !important;
  display: none;
  flex-direction: column;
  z-index: 10001;
  opacity: 0;
  transition: none !important;
  transform: translateY(100%);
}

#mobile-app-viewer.visible{opacity:1;transform:translateY(0)}

#mobile-app-close {
  position: absolute;
  top: 3%;
  right: 4%;
  width: clamp(28px,8vw,36px);
  height: clamp(28px,8vw,36px);
  background: #4a4a4a !important;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  transition: none !important;
  border: 3px solid #2a2a2a !important;
  box-shadow: 4px 4px 0 rgba(0,0,0,0.3) !important;
}

#mobile-app-close:active {
  box-shadow: 2px 2px 0 rgba(0,0,0,0.4) !important;
  transform: translate(2px, 2px);
}

#mobile-app-close svg{width:50%;height:50%;color:white}
#mobile-app-content{flex:1;display:flex;flex-direction:column;overflow:hidden;padding-top:8%}
#mobile-app-media-area{height:70%;display:flex;align-items:center;justify-content:center;padding:2%;overflow:hidden}
#mobile-app-media-area>*{max-width:100%;max-height:100%;object-fit:contain}
#mobile-app-media-area iframe,#mobile-app-media-area video{width:100%;height:100%;border:3px solid #2a2a2a !important}

#mobile-app-media-area pre {
  width: 100%;
  height: 100%;
  overflow: auto;
  background: #6b6b6b !important;
  padding: 4%;
  font-size: 9px;
  line-height: 1.4;
  white-space: pre-wrap;
  word-break: break-word;
  border: 3px solid #2a2a2a !important;
}

#mobile-app-info-area {
  height: 30%;
  overflow-y: auto;
  padding: 3% 5%;
  background: #4a4a4a !important;
}

#mobile-app-title {
  font-size: 9px;
  font-weight: 700;
  color: white;
  margin-bottom: 4px;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}

#mobile-app-description{font-size:9px;color:rgba(255,255,255,0.8);line-height:1.4;margin-bottom:8px}
.mobile-app-detail{font-size:9px;color:rgba(255,255,255,0.7);margin-bottom:2px}
.mobile-app-detail span{color:rgba(255,255,255,0.5)}
#mobile-app-links{margin-top:8px;display:flex;flex-wrap:wrap;gap:6px}
.mobile-app-link{font-size:9px;color:#6b6b6b;text-decoration:underline;cursor:pointer}
#mobile-app-swipe-indicator{width:15%;height:4px;background:#2a2a2a;margin:8px auto}
.mobile-glb-container{width:100%;height:100%;position:relative}
.mobile-glb-container canvas{width:100% !important;height:100% !important}

/* DESKTOP BRUTAL */
@media (min-width:769px){
  .finder-window{display:none !important}
  #circular-navigation{display:flex !important}
}

#desktop-icons{z-index:100 !important}

#circular-navigation {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  z-index: 1;
  background: transparent !important;
}

#circular-navigation::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  background: var(--desktop-bg);
  opacity: 1;
  transition: none !important;
}

.sidebar-spacer{flex-grow:1;max-height:15vh;min-height:20px}

#sidebar-scroll-wrapper {
  flex: 1;
  overflow-y: auto;
  pointer-events: auto;
  padding-right: 10px;
  min-height: 0;
}

#circular-sidebar {
  position: fixed;
  left: 0;
  top: 0;
  width: 420px;
  height: 100vh;
  padding: 40px;
  padding-top: 0;
  z-index: 10000;
  pointer-events: none;
  display: flex;
  flex-direction: column;
  background: rgba(74,74,74,0.3);
  border-right: 3px solid #2a2a2a;
}

#sidebar-top-section{width:100%;height:400px;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:30px}
#parametric-plan-container{width:110%;margin-left:-5%;aspect-ratio:1;background:transparent;padding:0;pointer-events:none;flex-shrink:0;z-index:50;opacity:0;visibility:hidden;transition:none !important}
#parametric-plan-container.visible{opacity:1;visibility:visible;pointer-events:auto}
.plan-room-shape:hover{fill-opacity:0.6 !important;transition:none !important}
#parametric-plan-container svg{width:100%;height:100%;overflow:visible;filter:drop-shadow(4px 4px 0 rgba(0,0,0,0.5))}
.plan-corridor-link{stroke-linecap:butt;stroke-linejoin:miter;fill:none;stroke-width:5px;opacity:0.65 !important;transition:none !important}
.plan-room-shape{stroke:#ffffff;stroke-width:2px;stroke-opacity:1;fill-opacity:1;transition:none !important}
.plan-room-shape.active{opacity:0.9 !important;fill-opacity:0.8 !important;stroke-opacity:1 !important;stroke-width:3px}
.plan-room-shape.inactive{opacity:0.2 !important}
.plan-membrane-outline{display:none}

#circular-sidebar-title {
  flex-shrink: 0;
  font-size: 34px;
  font-weight: 700;
  color: white;
  text-shadow: 3px 3px 0 rgba(0,0,0,0.8);
  margin-bottom: 20px;
  line-height: 1.1;
  letter-spacing: -0.02em;
  text-transform: uppercase;
}

#circular-sidebar-description {
  font-size: 13px;
  color: rgba(255,255,255,0.9);
  text-shadow: 2px 2px 0 rgba(0,0,0,0.8);
  line-height: 1.6;
  text-align: justify;
  text-align-last: left;
  margin-bottom: 24px;
  pointer-events: auto;
}

#circular-sidebar-links{font-size:14px;color:rgba(255,255,255,0.9)}

.sidebar-link-item {
  margin-bottom: 8px;
  padding: 10px 14px;
  background: #4a4a4a !important;
  border: 3px solid #2a2a2a !important;
  transition: none !important;
  cursor: pointer;
  box-shadow: 6px 6px 0 rgba(0,0,0,0.3) !important;
  pointer-events: auto;
}

.sidebar-link-item:hover {
  background: #1a1a1a !important;
  box-shadow: 8px 8px 0 rgba(0,0,0,0.4) !important;
}

.sidebar-link-name {
  font-weight: 700;
  color: white;
  margin-bottom: 4px;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}

.sidebar-link-desc{font-size:12px;color:rgba(255,255,255,0.7);line-height:1.4}

.plan-label {
  pointer-events: none !important;
  text-anchor: middle;
  dominant-baseline: central;
  alignment-baseline: central;
  fill: #ffffff !important;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.9);
  font-family: 'Space Grotesk', Arial, sans-serif !important;
  transition: none !important;
  transform-box: fill-box;
  transform-origin: center;
  stroke: #000000;
  stroke-width: 2px;
  stroke-linejoin: miter;
  paint-order: stroke fill;
}

.plan-label-main{font-size:16px;font-weight:900;fill:#ffffff !important;text-shadow:0 0 8px rgba(0,0,0,1),0 0 4px rgba(0,0,0,1)}
.plan-label-hub{font-size:11px;font-weight:700;fill:#ffffff !important;text-shadow:0 0 5px rgba(0,0,0,0.8)}
.plan-label-room{display:block;font-size:16px;font-weight:700;letter-spacing:-0.02em;fill:rgba(255,255,255,0.9) !important;text-shadow:0 0 3px rgba(0,0,0,0.8);text-transform:uppercase}

#circular-breadcrumb {
  position: fixed;
  bottom: 30px;
  left: 174px;
  font-size: 12px;
  color: white;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.5);
  z-index: 15000;
  pointer-events: none;
  font-family: 'Space Grotesk', monospace;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: -0.01em;
}

/* REMOVED - BACKGROUND SELECTOR DELETED */
#background-selector {
  display: none !important;
}

#layout-toggle-container {
  position: fixed;
  bottom: 26px;
  left: 30px;
  display: flex;
  gap: 6px;
  z-index: 15000;
  pointer-events: auto;
}

.layout-toggle-btn {
  width: 28px;
  height: 28px;
  background: #4a4a4a !important;
  border: 3px solid #2a2a2a !important;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: none !important;
  box-shadow: 4px 4px 0 rgba(0,0,0,0.3) !important;
}

.layout-toggle-btn:hover {
  background: #1a1a1a !important;
  box-shadow: 6px 6px 0 rgba(0,0,0,0.4) !important;
}

.layout-toggle-btn.active {
  background: #1a1a1a !important;
  border-color: #ffffff !important;
}

.layout-toggle-btn svg{width:16px;height:16px;color:white}

#toggle-plan-btn {
  min-width: 42px;
  width: 42px;
  font-size: 10px;
  font-weight: 700;
  color: white;
  text-transform: uppercase;
  letter-spacing: -0.01em;
}

#circular-back-button {
  position: fixed;
  top: 40px;
  left: 40px;
  width: 56px;
  height: 56px;
  background: #4a4a4a !important;
  border: 3px solid #2a2a2a !important;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 15000;
  transition: none !important;
  opacity: 0;
  pointer-events: none;
  box-shadow: 6px 6px 0 rgba(0,0,0,0.3) !important;
}

#circular-back-button.visible{opacity:1;pointer-events:all}

#circular-back-button:hover {
  background: #1a1a1a !important;
  box-shadow: 8px 8px 0 rgba(0,0,0,0.4) !important;
}

#circular-back-button svg{width:24px;height:24px;color:white}

#circular-container {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: none !important;
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}

#circular-container.dragging{cursor:grabbing !important}

.circular-scene {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transform: scale(1.2);
  transition: opacity 0.2s step-end, transform 0.2s step-end;
  will-change: transform, opacity;
  transform-origin: center center;
}

.circular-scene.active{opacity:1;pointer-events:all;transform:scale(1) !important}
.circular-scene.zoom-in-exit{opacity:0;transform:scale(1.5) !important;pointer-events:none}
.circular-scene.zoom-in-enter{opacity:0;transform:scale(0.5)}
.circular-scene.zoom-out-exit{opacity:0;transform:scale(0.5) !important;pointer-events:none}
.circular-scene.zoom-out-enter{opacity:0;transform:scale(2)}

.circular-item {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: none !important;
}

/* BRUTAL ICON WITH NOISE OVERLAY */
.circular-item-icon {
  background: #4a4a4a !important;
  border: 3px solid #2a2a2a !important;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  box-shadow: 8px 8px 0 rgba(0,0,0,0.3) !important;
  transition: none !important;
  position: relative;
}

.circular-item-icon::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise2'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' /%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise2)' opacity='0.3'/%3E%3C/svg%3E");
  pointer-events: none;
  mix-blend-mode: overlay;
  z-index: 1;
}

.circular-item:hover .circular-item-icon {
  box-shadow: 12px 12px 0 rgba(0,0,0,0.4) !important;
  background: #1a1a1a !important;
  border-color: #ffffff !important;
}

.circular-item-icon img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: grayscale(0.9) contrast(1.3) !important;
  mix-blend-mode: multiply;
}

.circular-item-icon svg {
  width: 60%;
  height: 60%;
  color: white;
  filter: drop-shadow(2px 2px 0 rgba(0,0,0,0.5));
}

.circular-item-name {
  margin-top: 12px;
  font-weight: 700;
  color: white;
  text-shadow: 2px 2px 0 rgba(0,0,0,0.5);
  text-align: center;
  overflow-wrap: break-word;
  word-wrap: break-word;
  hyphens: auto;
  line-height: 1.3;
  white-space: normal;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}
"""

# Replace the style content
new_content = content.replace(f'<style>{old_style}</style>', f'<style>{brutal_style}</style>')

# Also remove the background selector div from HTML
new_content = re.sub(
    r'<div id="background-selector">.*?</div>',
    '',
    new_content,
    flags=re.DOTALL
)

# Write the new file
with open('/home/user/dfw/index-beton.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ BRUTAL design applied successfully!")
print("✅ Background selector REMOVED")
print("✅ Concrete texture + directional light added")
print("✅ All border-radius removed")
print("✅ Heavy borders (3px solid #2a2a2a) applied")
print("✅ Hard shadows (8px 8px 0) applied")
print("✅ Monochrome palette applied")
print("✅ Space Grotesk + Inter fonts applied")
print("✅ Icon filters (grayscale + contrast + noise) applied")
print("✅ Brutal scrollbar (12px, blocky) applied")
