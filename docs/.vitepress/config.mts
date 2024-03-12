import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "LittleLab",
  description: "An Ansible project to automate your own self-hosted server",
  base: '/littlelab/',
  markdown: { theme: { light: 'vitesse-light', dark: 'vitesse-dark'} },
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Guide', link: '/introduction' }
    ],

    sidebar: [
      {
        text: 'Getting started',
        items: [
          { text: 'Introduction', link: '/introduction' },
          { text: 'Installation', link: '/installation' },
          { text: 'Setting up the inventory', link: '/inventory' },
          { text: 'Secrets management', link: '/secrets-management' },
          { text: 'Variables', link: '/variables' },
        ]
      },
      {
        text: 'Running',
        items: [
          { text: 'Initial setup', link: '/initial' },
          { text: 'Using the main playbook', link: '/main-playbook' },
          { text: 'Deploying specific services', link: '/playbooks' },
          { text: 'Creating new services', link: '/new-service' },
          { text: 'Creating new users', link: '/new-user' },
        ]
      },
      {
        text: 'Tools',
        items: [
          { text: 'Generating keys', link: '/generating-keys'},
          { text: 'Updating container images', link: '/container-update' },
        ]
      },
      {
        text: 'Roles',
        items: [
          { text: 'nginx', link: '/roles/nginx'},
          { text: 'setup_nginx', link: '/roles/setup_nginx'},
          { text: 'setup_sshd', link: '/roles/setup_sshd'},
        ]
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/mstcl/littlelab' }
    ]
  }
})
