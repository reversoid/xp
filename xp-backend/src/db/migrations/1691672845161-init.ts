import { MigrationInterface, QueryRunner } from 'typeorm';

export class Init1691672845161 implements MigrationInterface {
  name = 'Init1691672845161';

  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(
      `CREATE TABLE "observation" ("id" SERIAL NOT NULL, "text" text, "tg_photo_id" character varying(256), "tg_document_id" character varying(256), "tg_voice_id" character varying(256), "tg_video_id" character varying(256), "tg_video_note_id" character varying(256), "file_urls" character varying(256) array, "tg_media_group" jsonb array, "created_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "deleted_at" TIMESTAMP WITH TIME ZONE, "userId" integer NOT NULL, CONSTRAINT "PK_77a736edc631a400b788ce302cb" PRIMARY KEY ("id"))`,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_c485c6aa0770c9895923f47db9" ON "observation" ("created_at") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_64c2d8c59ee51c0c32a7a42836" ON "observation" ("deleted_at") `,
    );
    await queryRunner.query(
      `CREATE TABLE "user" ("id" SERIAL NOT NULL, "tg_id" bigint, "username" character varying(32), "password_hash" character(60) NOT NULL, "created_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "deleted_at" TIMESTAMP WITH TIME ZONE, CONSTRAINT "UQ_b49f86c002c69c1203e10bdfcf9" UNIQUE ("tg_id"), CONSTRAINT "UQ_78a916df40e02a9deb1c4b75edb" UNIQUE ("username"), CONSTRAINT "PK_cace4a159ff9f2512dd42373760" PRIMARY KEY ("id"))`,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_d091f1d36f18bbece2a9eabc6e" ON "user" ("created_at") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_22b81d3ed19a0bffcb660800f4" ON "user" ("deleted_at") `,
    );
    await queryRunner.query(
      `CREATE TYPE "public"."experiment_status_enum" AS ENUM('STARTED', 'COMPLETED', 'CANCELED')`,
    );
    await queryRunner.query(
      `CREATE TABLE "experiment" ("id" SERIAL NOT NULL, "text" text, "tg_photo_id" character varying(256), "tg_video_id" character varying(256), "tg_video_note_id" character varying(256), "tg_voice_id" character varying(256), "tg_document_id" character varying(256), "tg_media_group" jsonb array, "geo" jsonb, "status" "public"."experiment_status_enum" NOT NULL DEFAULT 'STARTED', "completed_at" TIMESTAMP WITH TIME ZONE, "complete_by" TIMESTAMP WITH TIME ZONE NOT NULL, "file_urls" character varying(256) array, "created_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "deleted_at" TIMESTAMP WITH TIME ZONE, "userId" integer NOT NULL, CONSTRAINT "PK_4f6eec215c62eec1e0fde987caf" PRIMARY KEY ("id"))`,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_9ca948c2bcec27a41f177a39a0" ON "experiment" ("status") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_779b5dfa1e540c3749eeb2e3e6" ON "experiment" ("completed_at") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_fb161369d6daa831f63ff96c61" ON "experiment" ("complete_by") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_b77c18fbb0806d18b3156803b4" ON "experiment" ("created_at") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_a181b9253bf626ec6d1826304e" ON "experiment" ("deleted_at") `,
    );
    await queryRunner.query(
      `ALTER TABLE "observation" ADD CONSTRAINT "FK_95e7f729cee52110c1f9a9e719d" FOREIGN KEY ("userId") REFERENCES "user"("id") ON DELETE CASCADE ON UPDATE NO ACTION`,
    );
    await queryRunner.query(
      `ALTER TABLE "experiment" ADD CONSTRAINT "FK_efd004fa410567831df8dd764fb" FOREIGN KEY ("userId") REFERENCES "user"("id") ON DELETE CASCADE ON UPDATE NO ACTION`,
    );
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(
      `ALTER TABLE "experiment" DROP CONSTRAINT "FK_efd004fa410567831df8dd764fb"`,
    );
    await queryRunner.query(
      `ALTER TABLE "observation" DROP CONSTRAINT "FK_95e7f729cee52110c1f9a9e719d"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_a181b9253bf626ec6d1826304e"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_b77c18fbb0806d18b3156803b4"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_fb161369d6daa831f63ff96c61"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_779b5dfa1e540c3749eeb2e3e6"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_9ca948c2bcec27a41f177a39a0"`,
    );
    await queryRunner.query(`DROP TABLE "experiment"`);
    await queryRunner.query(`DROP TYPE "public"."experiment_status_enum"`);
    await queryRunner.query(
      `DROP INDEX "public"."IDX_22b81d3ed19a0bffcb660800f4"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_d091f1d36f18bbece2a9eabc6e"`,
    );
    await queryRunner.query(`DROP TABLE "user"`);
    await queryRunner.query(
      `DROP INDEX "public"."IDX_64c2d8c59ee51c0c32a7a42836"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_c485c6aa0770c9895923f47db9"`,
    );
    await queryRunner.query(`DROP TABLE "observation"`);
  }
}
